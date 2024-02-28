from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class Exam(BaseModel):
    id: int
    name: str
    questions: [str]


class User(UserBase):
    id: int
    username: str
    password: str
    is_active: bool
    exams: [Exam] = []

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: str
    text: str
    options: [str]


class Submission(BaseModel):
    username: str
    exam_id: int
    answers: [str]

