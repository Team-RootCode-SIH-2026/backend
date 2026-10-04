import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.audio import AudioFile, AudioFileType
from ..models.images import ImageFile, ImageFileType
from ..models.text import TextFile, TextFileType
from ..models.user import User
from ..schemas.user import UserCreate


# For users
async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> User | None:
    result = await db.execute(select(User).where(User.pk_id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, user_email: str) -> User | None:
    result = await db.execute(select(User).where(User.k_email == user_email))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
    result = await db.execute(select(User).where(User.k_username == username))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user = User(
        k_email=user_in.email,
        k_username=user_in.username,
        hashed_pwd=user_in.password
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

# For files
async def create_audio_file_record(
    db: AsyncSession,
    *,
    owner_id: uuid.UUID,
    original_filename: str,
    stored_filename: str,
    category: AudioFileType,
    size_bytes: int
):
    file_record = AudioFile(
        fk_owner_id = owner_id,
        original_filename=original_filename,
        stored_filename=stored_filename,
        size_bytes=size_bytes,
        file_type=category,
        language_name="Unprocessed"
    )
    db.add(file_record)
    await db.commit()
    await db.refresh(file_record)
    return file_record


async def create_image_file_record(
    db: AsyncSession,
    *,
    owner_id: uuid.UUID,
    original_filename: str,
    stored_filename: str,
    category: ImageFileType,
    size_bytes: int
):
    file_record = ImageFile(
        fk_owner_id = owner_id,
        original_filename=original_filename,
        stored_filename=stored_filename,
        size_bytes=size_bytes,
        file_type=category,
        language_name="Unprocessed"
    )
    db.add(file_record)
    await db.commit()
    await db.refresh(file_record)
    return file_record

async def create_text_file_record(
    db: AsyncSession,
    *,
    owner_id: uuid.UUID,
    original_filename: str,
    stored_filename: str,
    category: TextFileType,
    size_bytes: int
):
    file_record = TextFile(
        fk_owner_id = owner_id,
        original_filename=original_filename,
        stored_filename=stored_filename,
        size_bytes=size_bytes,
        file_type=category,
        language_name="Unprocessed"
    )
    db.add(file_record)
    await db.commit()
    await db.refresh(file_record)
    return file_record


async def get_audio_file_by_id(db: AsyncSession, file_id: uuid.UUID):
    result = await db.execute(select(AudioFile).where(AudioFile.pk_id == file_id))
    return result.scalar_one_or_none()

async def get_image_file_by_id(db: AsyncSession, file_id: uuid.UUID):
    result = await db.execute(select(ImageFile).where(ImageFile.pk_id == file_id))
    return result.scalar_one_or_none()

async def get_text_file_by_id(db: AsyncSession, file_id: uuid.UUID):
    result = await db.execute(select(TextFile).where(TextFile.pk_id == file_id))
    return result.scalar_one_or_none()

async def get_audio_files_by_language(db: AsyncSession, language: str):
    result = await db.execute(select(AudioFile).where(AudioFile.language_name == language))
    return result.all()

async def get_image_files_by_language(db: AsyncSession, language: str):
    result = await db.execute(select(ImageFile).where(ImageFile.language_name == language))
    return result.all()

async def get_text_files_by_language(db: AsyncSession, language: str):
    result = await db.execute(select(TextFile).where(TextFile.language_name == language))
    return result.all()


async def delete_audio_file_record(db: AsyncSession, record: AudioFile):
    await db.delete(record)
    await db.commit()
