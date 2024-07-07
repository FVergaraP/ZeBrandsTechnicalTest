from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, verify_user
from app.schemas.product_schemas import ProductBase
from app.services import products_services

router = APIRouter()


@router.post("/products/", dependencies=[Depends(verify_user)])
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    return products_services.create_product(db=db, product=product)


@router.get("/products/")
def get_products(db: Session = Depends(get_db)):
    return products_services.get_products(db)


@router.patch("/products/", dependencies=[Depends(verify_user)])
async def update_product(product: ProductBase, db: Session = Depends(get_db)):
    return await products_services.update_product(db, product=product)


@router.delete("/products/{sku}", dependencies=[Depends(verify_user)])
def delete_product(sku: str, db: Session = Depends(get_db)):
    return products_services.delete_product(db, sku=sku)
