# main.py
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows requests from these origins
    allow_credentials=True,           # Allows cookies to be included in requests
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)
questions = [
    "Is the check engine light on?",
    "Are you hearing unusual noises while driving?",
    "Is the vehicle overheating?",
    "Does the vehicle have trouble starting?",
    "Are there any leaks under the vehicle?",
    "Is there a loss of power while accelerating?",
    "Have you noticed any unusual smells?",
    "Do the brakes feel spongy or unresponsive?",
]

@app.get("/question")
async def get_random_question():
    # Return a random question from the list
    question = random.choice(questions)
    return {"question": question}
