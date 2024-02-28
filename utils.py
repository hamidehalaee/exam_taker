# Create utility functions to:
# Read a single user by ID and by email.
# Read multiple users.
# Read multiple items.
from sqlalchemy.orm import Session
import models
import schemas
import secrets
import string
import bcrypt

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def generate_password():
    alphanumeric = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(alphanumeric) for i in range(10))
        if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit for c in password) >= 3
        ):
            break
    return password


def hash_password(password: str):
    """Generates a hashed version of the provided password."""
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def check_password(self, password):
    return bcrypt.checkpw(password.encode("utf-8"), self.password)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_exams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exam).offset(skip).limit(limit).all()


def create_user_exam(db: Session, exam: schemas.UserCreate, user_id: int):
    db_exam = models.Exam(**exam.dict(), owner_id=user_id)
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam
