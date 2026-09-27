import os
import json
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz(topic):
    prompt = f"""
Create a quiz about: {topic}

Generate exactly 3 multiple-choice questions.

Each question must have:
- 4 options
- 1 correct answer

Return ONLY valid JSON in this format:

[
    {{
        "question": "Question here",
        "options": ["A", "B", "C", "D"],
        "answer": "Correct option"
    }}
]
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return json.loads(response.text)