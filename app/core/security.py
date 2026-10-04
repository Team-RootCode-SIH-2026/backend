from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher

from .config import settings

pwd_context = PasswordHasher()

def hash(pwd: str) -> str:
    return pwd_context.hash(pwd)

def verify(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def _create_token(subject: str, expires_delta: timedelta, type: str):
    now = datetime.now(tz=timezone.utc)
    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + expires_delta,
        "type": type
    }
    return jwt.encode(payload=payload, key=settings.SEKRIT_KEY, algorithm=settings.ALGORITHM)

def create_access_token(subject: str):
    return _create_token(subject, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRY_MIN), type="access")

def create_refresh_token(subject: str):
    return _create_token(subject, timedelta(days=settings.REFRESH_TOKEN_EXPIRY_DAYS), type="refresh")

def decode_token(tok: str) -> dict:
    return jwt.decode(tok, settings.SEKRIT_KEY, algorithms=[settings.ALGORITHM])

