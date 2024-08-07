from sqlalchemy import Column, String, REAL, Boolean

from app.config.database import Base


class Product(Base):
    __tablename__ = "products"

    sku = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    brand = Column(String)
    price = Column(REAL)
    deleted = Column(Boolean, default=False)


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, unique=True, index=True)
    disable = Column(Boolean, default=False)
