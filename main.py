from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Mock database models
class User(BaseModel):
    username: str
    password: str

class Exam(BaseModel):
    id: int
    name: str
    questions: List[str]

class Question(BaseModel):
    id: str
    text: str
    options: List[str]

class Submission(BaseModel):
    username: str
    exam_id: int
    answers: List[str]

# Mock database
users_db = []
exams_db = []
submissions_db = []

# Utility functions
def get_user(username: str):
    for user in users_db:
        if user.username == username:
            return user
    return None

def get_exam(exam_id: int):
    for exam in exams_db:
        if exam.id == exam_id:
            return exam
    return None

# Routes
@app.post("/users/")
async def create_user(user: User):
    users_db.append(user)
    return user

@app.post("/exams/")
async def create_exam(exam: Exam):
    exams_db.append(exam)
    return exam

@app.get("/exams/{exam_id}/questions/")
async def get_exam_questions(exam_id: int):
    exam = get_exam(exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam.questions

@app.post("/submit/")
async def submit_exam(submission: Submission):
    user = get_user(submission.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    exam = get_exam(submission.exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    
    if len(submission.answers) != len(exam.questions):
        raise HTTPException(status_code=400, detail="Invalid number of answers")
    
    submissions_db.append(submission)
    return submission
