from google import genai
import pyaudio
from google.genai import types
from tools.all_tools import FUNCTIONS
from dotenv import load_dotenv
import os
import asyncio
from RealtimeSTT import AudioToTextRecorder

load_dotenv()

class AudioAssistant:
    def __init__(self, name="Charlie"):
        self.name = name
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"),
                               http_options={'api_version': 'v1alpha'})
        self.model = "gemini-2.0-flash-exp"
        self.config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            tools=list(FUNCTIONS.values()) + [{"google_search": {}}],
            system_instruction=types.Content(
                parts=[
                    types.Part(
                        text=f"You are a Jarvis-like assistant '{self.name}'. You can do anything the user asks you to do with the tools you have. answer in a friendly tone. Don't give long responses. Give only SHORT responses.",
                    )
                ]
            ),
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Aoede")
                )
            ),
        )
        self.p = pyaudio.PyAudio()
        self.prev_prompt = ""
        self.awake = False

    async def _async_enumerate(self, it):
        n = 0
        async for item in it:
            yield n, item
            n += 1

    async def _handle_tool_call(self, session, tool_call):
        for fc in tool_call.function_calls:
            if fc.name in FUNCTIONS:
                f = FUNCTIONS[fc.name]
                tool_response = types.LiveClientToolResponse(
                    function_responses=[
                        types.FunctionResponse(
                            name=fc.name,
                            id=fc.id,
                            response=f(**fc.args),
                        )
                    ]
                )
                await session.send(input=tool_response)
            else:
                print(f"Error: Function '{fc.name}' not found.")

    async def audio_mode(self, recorder):
        while True:
            print("SESSION STARTED!")
            async with self.client.aio.live.connect(model=self.model, config=self.config) as session:
                while True:
                    if self.prev_prompt:
                        message = self.prev_prompt
                        self.prev_prompt = ""
                    else:
                        message = recorder.text()
                    try:
                        stream = self.p.open(format=self.p.get_format_from_width(2),
                                        channels=1,
                                        rate=24000,
                                        output=True)
                        recorder.stop()
                        if self.name.lower() in message.lower() or self.awake:
                            self.awake = True
                            await session.send(input=message, end_of_turn=True)
                            async for idx, response in self._async_enumerate(session.receive()):
                                if response.text is not None:
                                    print(response.text, end="")
                                if response.tool_call is not None:
                                    await self._handle_tool_call(session, response.tool_call)
                                if response.data is not None: 
                                    stream.write(response.data)
                            if 'bye' in message.lower():
                                self.awake = False
                        stream.close()
                    except Exception as e:
                        self.prev_prompt = message
                        print(e)
                        break

if __name__ == "__main__":
    recorder = AudioToTextRecorder(language="en", spinner=True, ensure_sentence_ends_with_period=True)
    assistant = AudioAssistant()
    while True:
        try:
            asyncio.run(assistant.audio_mode(recorder))
        except Exception as e:
            print(type(e), e)