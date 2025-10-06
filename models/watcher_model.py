from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
import base64

load_dotenv()

def generate():
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

if __name__ == "__main__":
    generate()