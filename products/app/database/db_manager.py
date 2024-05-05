from sqlalchemy.orm import Session

from app.database import models
from app.schemas.product_schemas import ProductBase


def get_product_by_sky(db: Session, sku: str):
    return db.query(models.Product).filter(models.Product.sku == sku).first()


def create_product(db: Session, product: ProductBase):
    db_product = models.Product(
        sku=product.sku,
        name=product.name,
        price=product.price,
        brand=product.brand,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db):
    return db.query(models.Product).all()
