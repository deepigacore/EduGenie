import os
from google import genai

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def summarize_text(text):

    prompt = f"""
You are EduGenie, an AI learning assistant.

Summarize the following text:

"{text}"

STRICT RESPONSE RULES:

1. Give a concise summary.
2. Use clear bullet points.
3. Each bullet should contain only one main idea.
4. Keep each bullet short and easy to understand.
5. Include only the important information.
6. Remove repetition and unnecessary details.
7. Do not write long paragraphs.
8. Keep the summary suitable for quick revision.
9. Do not use ###, **, ---, or decorative Markdown.
10. Do not add information that is not present in the original text.

Format:

• Main point
• Main point
• Main point
• Main point

Use as many bullets as necessary, but keep the overall summary concise.

Return only the summary.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return "Unable to summarize the text: " + str(e)