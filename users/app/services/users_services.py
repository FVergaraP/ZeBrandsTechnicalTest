import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.config.logger import get_custom_logger
from app.database import db_manager
from app.schemas.user_schemas import UserToken, UserCredential, UserCreate
from app.utils.authentication import create_access_token
from app.utils.constants.error import USER_NOT_FOUND, EMAIL_ALREADY_EXISTS, BAD_CREDENTIALS, DELETING_SUPERADMIN
from app.utils.encrypt import get_password_hash, verify_password

logger = get_custom_logger(logging.getLogger(__name__))


def create_user(db: Session, user: UserCreate):
    existing_user = db_manager.get_user_by_email(db, user.email)

    if existing_user:
        if existing_user.disable:
            return db_manager.enable_user(db, existing_user, get_password_hash(user.password))
        else:
            logger.error("The user with this email already exists")
            raise HTTPException(status_code=500, detail={"code": EMAIL_ALREADY_EXISTS})

    user.password = get_password_hash(user.password)
    return db_manager.create_user(db, user)


def delete_user(db: Session, user_email: str):
    db_user = db_manager.get_user_by_email(db, user_email)

    if not db_user:
        logger.error("The user with this email not exist")
        raise HTTPException(status_code=500, detail={"code": USER_NOT_FOUND})

    if db_user.superadmin:
        logger.error("The user is superadmin, cannot delete it")
        raise HTTPException(status_code=500, detail={"code": DELETING_SUPERADMIN})

    return db_manager.delete_user(db, db_user)


def change_password(db, user: UserCredential):
    existing_user = db_manager.get_user_by_email(db, user.email)

    if not existing_user or existing_user.disable:
        logger.error("The user with this email not exist")
        raise HTTPException(status_code=500, detail={"code": USER_NOT_FOUND})

    existing_user.password = get_password_hash(user.password)
    db.commit()
    return 'Password changed successfully'


def login(db: Session, user: UserCredential):
    existing_user = db_manager.get_user_by_email(db, user.email)

    if not existing_user or existing_user.disable:
        logger.error("The user with this email not exist")
        raise HTTPException(status_code=500, detail={"code": BAD_CREDENTIALS})

    if not verify_password(user.password, existing_user.password):
        logger.error("Invalid Password")
        raise HTTPException(status_code=500, detail={"code": BAD_CREDENTIALS})

    access_token = create_access_token(data={"sub": user.email})
    existing_user.access_token = access_token
    db.commit()

    return UserToken(access_token=access_token)
