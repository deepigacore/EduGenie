import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_learning_path(topic):
    prompt = f"""
Create a simple learning path for:

{topic}

Give only:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Practice activities
5. One small final project

Keep it short and student-friendly.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text