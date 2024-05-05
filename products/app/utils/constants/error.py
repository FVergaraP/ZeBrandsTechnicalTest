from fastapi import HTTPException

BAD_CREDENTIALS = "003"
BAD_CREDENTIALS_NOT_EMAIL = "004"
BAD_CREDENTIALS_NOT_USER = "005"

PRODUCT_ALREADY_EXISTS = "P001"
PRODUCT_NOT_EXISTS = "P002"


def credentials_exception(detail):
    return HTTPException(
        status_code=401,
        detail={"code": detail},
    )


def custom_internal_exception(detail):
    return HTTPException(
        status_code=500,
        detail={"code": detail},
    )
