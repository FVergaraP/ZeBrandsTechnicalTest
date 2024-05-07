import logging

from app.config.logger import get_custom_logger
from app.schemas.product_schemas import ProductBase

logger = get_custom_logger(logging.getLogger(__name__))


def notify_all_users(product: ProductBase, user):
    logger.info("Notifying all users")
    logger.info("Not Implemented Yet")
