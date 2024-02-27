#models from Pydantic
from pydantic import BaseModel, list



from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

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

