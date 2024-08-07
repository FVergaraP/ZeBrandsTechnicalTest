import logging

from fastapi import HTTPException, Request
from sqlalchemy.orm import Session

from app.config.logger import get_custom_logger
from app.database import db_manager
from app.schemas.product_schemas import ProductBase
from app.services.notify_services import notify_all_users
from app.utils.constants.error import PRODUCT_ALREADY_EXISTS, custom_internal_exception, PRODUCT_NOT_EXISTS, BAD_REQUEST

logger = get_custom_logger(logging.getLogger(__name__))


def create_product(db: Session, product: ProductBase):
    product_validaton(product)
    existing_product = db_manager.get_product_by_sky(db, product.sku)

    if existing_product:
        if existing_product.deleted:
            return db_manager.enable_product(db, existing_product)

        logger.error("There is already a product with sku {}".format(product.sku))
        raise custom_internal_exception(PRODUCT_ALREADY_EXISTS)

    return db_manager.create_product(db, product)


def get_products(db):
    return db_manager.get_products(db)


async def update_product(db, product):
    existing_product = db_manager.get_product_by_sky(db, product.sku)

    if not existing_product:
        logger.error("There is no product with sku {}".format(product.sku))
        raise custom_internal_exception(PRODUCT_NOT_EXISTS)

    existing_product.name = product.name
    existing_product.price = product.price

    db.commit()
    await notify_all_users(db, existing_product)
    return existing_product


def delete_product(db, sku):
    existing_product = db_manager.get_product_by_sky(db, sku)

    if not existing_product:
        logger.error("There is no product with sku {}".format(sku))
        raise custom_internal_exception(PRODUCT_NOT_EXISTS)

    return db_manager.delete_product(db, existing_product)

def product_validaton(product: ProductBase):
    if not product.name:
        logger.error("There is no product name")
        raise HTTPException(status_code=500, detail={"code": BAD_REQUEST})

    if not product.sku:
        logger.error("There is no product sku")
        raise HTTPException(status_code=500, detail={"code": BAD_REQUEST})

    if not product.brand:
        logger.error("There is no product brand")
        raise HTTPException(status_code=500, detail={"code": BAD_REQUEST})

    if not product.price:
        logger.error("There is no product price")
        raise HTTPException(status_code=500, detail={"code": BAD_REQUEST})