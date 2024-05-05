from datetime import datetime, timezone, timedelta

from jose import jwt

SECRET_KEY = "23b6ad5e880c25c3831e9977582dbb129609704fcad29bea85a0f23cb10a307e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
