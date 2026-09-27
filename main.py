import os

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/qa")
def question_answer(question: str = Form(...)):
    try:
        answer = answer_question(question)
        return {"answer": answer}

    except Exception as e:
        return {"answer": "Gemini error: " + str(e)}


@app.post("/explain")
def explain(question: str = Form(...)):
    try:
        answer = explain_topic(question)
        return {"answer": answer}

    except Exception as e:
        return {"answer": "Gemini error: " + str(e)}


@app.post("/quiz")
def quiz(question: str = Form(...)):
    try:
        answer = generate_quiz(question)
        return {"answer": answer}

    except Exception as e:
        return {"answer": "Gemini error: " + str(e)}


@app.post("/summarize")
def summarize(question: str = Form(...)):
    try:
        answer = summarize_text(question)
        return {"answer": answer}

    except Exception as e:
        return {"answer": "Gemini error: " + str(e)}


@app.post("/learn/recommendations")
def learning_path(question: str = Form(...)):
    try:
        answer = generate_learning_path(question)
        return {"answer": answer}

    except Exception as e:
        return {"answer": "Gemini error: " + str(e)}