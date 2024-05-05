import logging

from sqlalchemy.orm import Session

from app.config.logger import get_custom_logger
from app.database import db_manager
from app.schemas.product_schemas import ProductBase
from app.utils.constants.error import PRODUCT_ALREADY_EXISTS, custom_internal_exception

logger = get_custom_logger(logging.getLogger(__name__))


def create_product(db: Session, product: ProductBase):
    existing_product = db_manager.get_product_by_sky(db, product.sku)

    if existing_product:
        logger.error("There is already a product with sku {}".format(product.sku))
        raise custom_internal_exception(PRODUCT_ALREADY_EXISTS)

    return db_manager.create_product(db, product)
