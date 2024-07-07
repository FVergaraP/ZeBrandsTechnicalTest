import logging

from fastapi import Request

from app.config.logger import get_custom_logger
from app.services.authentication_services import get_user
from app.utils.constants.error import credentials_exception, BAD_CREDENTIALS, \
    BAD_CREDENTIALS_NOT_USER

logger = get_custom_logger(logging.getLogger(__name__))


async def verify_user(request: Request):
    try:
        token = request.headers.get("x-token")
        user = await get_user(token)
    except Exception as e:
        logger.error(e)
        raise credentials_exception(BAD_CREDENTIALS)

    if user is None:
        raise credentials_exception(BAD_CREDENTIALS_NOT_USER)
    request.state.user = user
