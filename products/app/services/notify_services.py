import logging
import httpx

from app.config.config import settings
from app.config.logger import get_custom_logger
from app.database.db_manager import get_users
from app.schemas.product_schemas import ProductBase

logger = get_custom_logger(logging.getLogger(__name__))


async def notify_all_users(db, product: ProductBase):
    logger.info("Notifying all users")
    users = get_users(db)
    emails = [user.email for user in users]
    api_url = settings.notify_service_url
    data = {
        "receipts": emails,
        "message": 'The product {0} was modified'.format(product.name),
        "subject": "Product updated"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, json=data)
        return response.json()
