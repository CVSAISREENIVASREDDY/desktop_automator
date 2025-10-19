from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import json

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

def get_summarize_text(link):
    response = llm.invoke(f"Explain me about this page content: {link}\n")
    return response.content


def get_xpath(rawHtml, element):
    parser = JsonOutputParser()

    prompt = PromptTemplate(
        template="""I will give the raw html and 'the thing that use want to interact like(open first link in google search page) or input field name username like that or searchbar' give me exact the xpath by only (href or id or text or unique identifier)
        UI element: {element}
        Raw html: {rawHtml}
        {format_instructions}
        """,
        input_variables=["element", "rawHtml"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser
    response = chain.invoke({"element": element, "rawHtml": rawHtml})
    return response 
