from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import *
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    exams = relationship("Exam", back_populates="owner")


class Exam(Base):
    __tablename__: str = "exams"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="exams")


class Question(Base):
    __tablename__:str = "question"

    id = Column(Integer, primary_key=True)
    text = Column(String, index=True)
    options = relationship("Option", back_populates="question")


class Option(Base):
    __tablename__ = "option"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", back_populates="option")


class Submission(base):
    __tablename__: str = "submission"

    username = Column(String, index=True)
    exam_id = Column(Integer, ForeignKey("exam.id"))
    answers = relationship("Answer", back_populates="submission")
