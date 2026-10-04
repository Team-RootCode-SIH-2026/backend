import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.audio import AudioFile
from ..models.images import ImageFile
from ..models.text import TextFile
from ..models.user import User




async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> User | None:
    result = await db.execute(select(User).where(User.pk_id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, user_email: str) -> User | None:
    result = await db.execute(select(User).where(User.k_email == user_email))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
    result = await db.execute(select(User).where(User.k_username == username))
    return result.scalar_one_or_none()

async def create_user()
