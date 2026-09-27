import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_topic(topic):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"Explain the following topic in simple and easy-to-understand language for a student:\n\n{topic}"
    )

    return response.text