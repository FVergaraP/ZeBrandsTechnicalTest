from sqlalchemy import Boolean, Column, String

from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, unique=True, index=True)
    full_name = Column(String)
    password = Column(String)
    access_token = Column(String)
    disable = Column(Boolean, default=False)
