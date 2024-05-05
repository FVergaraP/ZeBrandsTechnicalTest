import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.config.logger import get_custom_logger
from app.database import db_manager
from app.schemas import user_schemas
from app.utils.encrypt import get_password_hash

logger = get_custom_logger(logging.getLogger(__name__))


def get_user_by_email(db: Session, user_email: str):
    return db_manager.get_user_by_email(db, user_email)


def create_user(db: Session, user: user_schemas.UserCreate):
    existing_user = db_manager.get_user_by_email(db, user.email)
    if existing_user:
        logger.error("The user with this email already exists")
        raise HTTPException(status_code=400, detail="Email already registered")

    user.password = get_password_hash(user.password)

    return db_manager.create_user(db, user)
