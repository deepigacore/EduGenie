import os
from google import genai
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def answer_question(question):

    prompt = f"""
You are EduGenie, an AI learning assistant.

Answer the student's question:

"{question}"

STRICT RESPONSE RULES:

1. Give a CRISP and DIRECT answer.
2. Keep the answer short and easy to understand.
3. Normally use only 2–5 sentences.
4. Do NOT write long paragraphs.
5. Do NOT repeat the question.
6. Do NOT add unnecessary background information.
7. Use simple student-friendly language.
8. If a definition is asked, give the definition first.
9. If an example is useful, give only ONE short example.
10. Use bullet points only when they make the answer clearer.
11. Do not use markdown symbols such as ###, **, or ---.
12. Answer ONLY what the student asked.

Return only the final answer.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return "Unable to generate an answer: " + str(e)