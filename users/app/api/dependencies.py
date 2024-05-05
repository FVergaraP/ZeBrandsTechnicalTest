import logging

from fastapi import Request, Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.config.logger import get_custom_logger
from app.database import db_manager
from app.utils.constants.error import credentials_exception, BAD_CREDENTIALS_NOT_EMAIL, BAD_CREDENTIALS, \
    BAD_CREDENTIALS_NOT_USER

logger = get_custom_logger(logging.getLogger(__name__))

SECRET_KEY = "23b6ad5e880c25c3831e9977582dbb129609704fcad29bea85a0f23cb10a307e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_user(request: Request, db: Session = Depends(get_db)):
    try:
        token = request.headers.get("x-token")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception(BAD_CREDENTIALS_NOT_EMAIL)
    except JWTError as e:
        logger.error(e)
        raise credentials_exception(BAD_CREDENTIALS)
    user = db_manager.get_user_by_email(db, email)
    if user is None:
        raise credentials_exception(BAD_CREDENTIALS_NOT_USER)
    request.state.user = user
