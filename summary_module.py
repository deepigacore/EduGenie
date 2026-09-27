import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_text(text):
    prompt = f"""
Summarize the following text in a clear and simple way
for a student.

Text:
{text}

Give the summary using short paragraphs and important
points. Do not add information that is not present in
the original text.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text