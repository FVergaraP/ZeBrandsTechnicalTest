from sqlalchemy import Column, String, REAL

from app.config.database import Base


class Product(Base):
    __tablename__ = "products"

    sku = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    brand = Column(String)
    price = Column(REAL)
