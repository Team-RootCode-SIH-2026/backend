import secrets
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "Voices_Backside"
    DEBUG_MODE: bool = True

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/Voices_of_India"

    SEKRIT_KEY: bytes = secrets.token_bytes(32)

    ALGORITHM: str = "HS256"

    UPLOAD_DIR: str = "storage"
    MAX_UPLOAD_SIZE: int = 100 * 1024 * 1024     # Upload size on bytes (100 MB)

    ALLOWED_ORIGINS: str = "*"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

