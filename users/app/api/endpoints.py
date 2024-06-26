from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, verify_user
from app.schemas.user_schemas import UserToken, UserCredential, UserCreate, UserBase
from app.services import users_services

router = APIRouter()


@router.post("/users/", response_model=UserBase, dependencies=[Depends(verify_user)])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return users_services.create_user(db=db, user=user)

@router.get("/users/validate_token", response_model=UserBase, dependencies=[Depends(verify_user)])
def validate_token(request: Request):
    return request.state.user


@router.delete("/users/{user_email}", dependencies=[Depends(verify_user)])
def delete_user(user_email: str, db: Session = Depends(get_db)):
    return users_services.delete_user(db, user_email)


@router.patch("/users/change_password", dependencies=[Depends(verify_user)])
def change_password(user: UserCredential, db: Session = Depends(get_db)):
    return users_services.change_password(db=db, user=user)


@router.post("/users/login", response_model=UserToken)
def login_admin(user: UserCredential, db: Session = Depends(get_db)):
    return users_services.login(db=db, user=user)

