from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas import user_schemas
from app.services import users_services

router = APIRouter()


@router.post("/users/", response_model=user_schemas.UserCreate)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return users_services.create_user(db=db, user=user)


@router.delete("/users/{user_email}")
def delete_user(user_email: str, db: Session = Depends(get_db)):
    return users_services.delete_user(db, user_email)


@router.patch("/users/change_password")
def create_user(user: user_schemas.UserRefreshPassword, db: Session = Depends(get_db)):
    return users_services.change_password(db=db, user=user)


@router.get("/users/{user_email}", response_model=user_schemas.User)
def read_user(user_email: str, db: Session = Depends(get_db)):
    db_user = users_services.get_user_by_email(db, user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
