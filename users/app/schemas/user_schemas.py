from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: str


class UserCreate(UserBase):
    password: str


class UserRefreshPassword(BaseModel):
    email: str
    password: str


class User(UserBase):
    disable: bool

    class Config:
        orm_mode = True
