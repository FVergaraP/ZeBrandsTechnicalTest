from sqlalchemy.orm import Session

from app.database import db_manager


def get_user_by_email(db: Session, user_email: str):
    return db_manager.get_user_by_email(db, user_email)
