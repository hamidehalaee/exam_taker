#models from Pydantic
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class Exam(BaseModel):
    id: int
    name: str
    questions: list[str]

class User(UserBase):
    id: int
    username: str
    password: str
    is_active: bool
    exams: list[Exam] = []

    class Config:
        orm_mode = True

class Question(BaseModel):
    id: str
    text: str
    options: list[str]

class Submission(BaseModel):
    username: str
    exam_id: int
    answers: list[str]

