from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
import base64
from helpers import take_screenshot

load_dotenv()

def generate_description():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

    # Read the image file and encode it in base64
    with open("screenshot.png", "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    message = HumanMessage(
        content=[
            {"type": "text", "text": "Describe what's on my screen."},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image_data}"},
            },
        ]
    )

    response = llm.invoke([message])
    return response.content

def look_at_my_screen() -> dict:
    """
    Describes my current screen.
    """
    take_screenshot()
    print("WATCHER CALLED!")
    description = generate_description()
    print(description)
    return {"description": description} 