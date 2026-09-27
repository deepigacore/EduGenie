import os
from dotenv import load_dotenv
from google import genai
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def explain_topic(topic):

    prompt = f"""
You are EduGenie, an AI learning assistant.

Explain this topic:

"{topic}"

STRICT RESPONSE RULES:

1. Explain the topic clearly for a college student.
2. Make the explanation slightly detailed, but NOT too long.
3. Use 3–5 short sections or bullet points when appropriate.
4. Start with a simple definition or main idea.
5. Explain the important points in simple language.
6. Give ONE simple example if useful.
7. Avoid unnecessary information.
8. Do NOT write huge paragraphs.
9. Do NOT repeat the topic unnecessarily.
10. Do NOT use ###, **, ---, or other decorative Markdown symbols.
11. Keep the answer easy to read and revise for exams.

Recommended structure:

Definition:
Short explanation.

Key points:
• Point 1
• Point 2
• Point 3

Example:
One simple example, only if useful.

Return only the explanation.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return "Unable to explain the topic: " + str(e)