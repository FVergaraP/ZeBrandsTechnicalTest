from fastapi import HTTPException

USER_NOT_FOUND = "001"
EMAIL_ALREADY_EXISTS = "002"
BAD_CREDENTIALS = "003"
BAD_CREDENTIALS_NOT_EMAIL = "004"
BAD_CREDENTIALS_NOT_USER = "005"
DELETING_SUPERADMIN = "006"
BAD_REQUEST = "007"


def credentials_exception(detail):
    return HTTPException(
        status_code=401,
        detail={"code": detail},
    )
