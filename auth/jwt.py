import os

import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv("SHOPNEST_JWT_SECRET")

if not SECRET_KEY:
    raise RuntimeError("SHOPNEST_JWT_SECRET is not configured")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(user_id, role_id, role_name):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "role_id": role_id,
        "role_name": role_name,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "succeed": True,
            "data": payload
        }

    except jwt.ExpiredSignatureError:
        return {
            "succeed": False,
            "message": "Token has expired"
        }

    except jwt.InvalidTokenError:
        return {
            "succeed": False,
            "message": "Invalid token"
        }