import os
import json
from google import genai

from dotenv import load_dotenv
load_dotenv()


# Get Gemini API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_quiz(topic):

    prompt = f"""
You are EduGenie, an educational quiz generator.

The student wants a quiz about this EXACT topic:

"{topic}"

STRICT RULES:

1. Generate exactly 3 multiple-choice questions.
2. EVERY question must be directly related to the exact topic given above.
3. DO NOT generate questions from unrelated topics.
4. If the topic is "Pythagoras theorem", questions must be specifically
   about the Pythagorean theorem, right triangles, a² + b² = c²,
   finding missing sides, or applying the theorem.
5. Each question must have exactly 4 answer options.
6. Only ONE option must be correct.
7. Include the correct answer.
8. Questions should be suitable for a college/student learning level.
9. Make the questions different from each other.
10. Do not include explanations outside the JSON.
11. Return ONLY valid JSON.
12. Do not use Markdown code fences.
13. Do not add introductory or concluding text.

Use exactly this JSON structure:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option A"
  }},
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option B"
  }},
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option C"
  }}
]

Before returning the response, check that:
- All 3 questions are about "{topic}"
- Every question has exactly 4 options
- Every answer exactly matches one option
- There are no unrelated questions
- The response is valid JSON
"""


    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        text = response.text.strip()


        # Remove accidental Markdown fences
        if text.startswith("```"):

            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()


        # Validate JSON
        quiz = json.loads(text)


        # Make sure we received a list
        if not isinstance(quiz, list):

            raise ValueError(
                "Gemini did not return a quiz list."
            )


        # Make sure there are exactly 3 questions
        if len(quiz) != 3:

            raise ValueError(
                "Gemini did not generate exactly 3 questions."
            )


        # Validate every question
        for question in quiz:

            if not isinstance(question, dict):

                raise ValueError(
                    "Invalid question format."
                )


            if "question" not in question:

                raise ValueError(
                    "Question text is missing."
                )


            if "options" not in question:

                raise ValueError(
                    "Options are missing."
                )


            if "answer" not in question:

                raise ValueError(
                    "Correct answer is missing."
                )


            if not isinstance(
                question["options"],
                list
            ):

                raise ValueError(
                    "Options must be a list."
                )


            if len(question["options"]) != 4:

                raise ValueError(
                    "Every question must have exactly 4 options."
                )


            if question["answer"] not in question["options"]:

                raise ValueError(
                    "Correct answer does not match an option."
                )


        return json.dumps(
            quiz,
            ensure_ascii=False
        )


    except Exception as e:

        return json.dumps({
            "error": "Unable to generate quiz.",
            "details": str(e)
        })