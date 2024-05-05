from sqlalchemy.orm import Session

from app.database import models
from app.schemas import user_schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = models.User(email=user.email, password=user.password, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
