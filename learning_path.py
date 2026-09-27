import os
from google import genai
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_learning_path(topic):

    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a practical learning path for:

"{topic}"

STRICT RESPONSE RULES:

1. Make the learning path detailed enough to be genuinely useful.
2. Keep it organized and easy to follow.
3. Divide it into clear stages or steps.
4. Start with the basics before moving to advanced concepts.
5. Give a short explanation for each stage.
6. Include important concepts to learn at each stage.
7. Include practice suggestions where useful.
8. End with a small project or practical task.
9. Do NOT write huge paragraphs.
10. Use short bullet points.
11. Do NOT repeat the topic unnecessarily.
12. Do NOT add unrelated information.
13. Do not use ###, **, ---, or decorative Markdown symbols.

Use this structure:

Learning Path: [Topic]

Step 1 — Basics
• What to learn
• What to understand

Step 2 — Core Concepts
• Important concepts
• What to practice

Step 3 — Intermediate
• Concepts to study
• Practice ideas

Step 4 — Advanced
• Advanced concepts
• Practical application

Final Project
• One practical project to apply what was learned.

Return only the learning path.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return "Unable to generate a learning path: " + str(e)