import logging

from fastapi import Request
from sqlalchemy.orm import Session

from app.config.logger import get_custom_logger
from app.database import db_manager
from app.schemas.product_schemas import ProductBase
from app.services.notify_services import notify_all_users
from app.utils.constants.error import PRODUCT_ALREADY_EXISTS, custom_internal_exception, PRODUCT_NOT_EXISTS

logger = get_custom_logger(logging.getLogger(__name__))


def create_product(db: Session, product: ProductBase):
    existing_product = db_manager.get_product_by_sky(db, product.sku)

    if existing_product:
        if existing_product.deleted:
            return db_manager.enable_product(db, existing_product)

        logger.error("There is already a product with sku {}".format(product.sku))
        raise custom_internal_exception(PRODUCT_ALREADY_EXISTS)

    return db_manager.create_product(db, product)


def get_products(db):
    return db_manager.get_products(db)


def update_product(db, product, request: Request):
    existing_product = db_manager.get_product_by_sky(db, product.sku)

    if not existing_product:
        logger.error("There is no product with sku {}".format(product.sku))
        raise custom_internal_exception(PRODUCT_NOT_EXISTS)

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price

    db.commit()
    notify_all_users(existing_product, request.state.user)
    return existing_product


def delete_product(db, sku):
    existing_product = db_manager.get_product_by_sky(db, sku)

    if not existing_product:
        logger.error("There is no product with sku {}".format(sku))
        raise custom_internal_exception(PRODUCT_NOT_EXISTS)

    return db_manager.delete_product(db, existing_product)
