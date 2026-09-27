# EduGenie – AI Learning Assistant

EduGenie is an AI-powered learning assistant designed to help students learn concepts easily using Google Gemini.

## Features

- Ask – Get answers to academic questions.
- Explain – Understand difficult concepts in simple language.
- Quiz – Generate quizzes for practice.
- Summarize – Get concise summaries of study material.
- Learning Path – Get personalized learning recommendations.
- Voice Input – Ask questions using your voice.
- Read Aloud – Listen to generated answers.

## Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript
- Jinja2
- Uvicorn

## Project Structure

EduGenie/
│
├── main.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
└── README.md

## Installation

### 1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

cd EduGenie

### 2. Install the Required Packages

pip install -r requirements.txt

### 3. Set the Gemini API Key

Create an environment variable named:

GEMINI_API_KEY

Do not publish your API key in the repository.

### 4. Run the Application

uvicorn main:app --reload

### 5. Open the Application

Open the following address in your browser:

http://127.0.0.1:8000

## Project Goal

The goal of EduGenie is to provide students with an interactive AI-based learning environment for understanding concepts, practicing through quizzes, summarizing study material, and creating personalized learning paths.

## Future Enhancements

- User accounts and learning history
- Progress tracking
- More personalized recommendations
- Support for additional AI models
- Mobile-friendly application
- Voice-based learning interaction

## Developed By

Deepiga
