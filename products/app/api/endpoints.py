from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, verify_user
from app.schemas.product_schemas import ProductBase
from app.services import products_services

router = APIRouter()


@router.post("/products/", response_model=ProductBase, dependencies=[Depends(verify_user)])
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    return products_services.create_product(db=db, product=product)
