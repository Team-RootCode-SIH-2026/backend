from __future__ import annotations

import uuid
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .files import UploadedFile
from .languages import Languages

if TYPE_CHECKING:
    from .user import User

class AudioFileType(str, Enum):
    mp3 = "mp3"
    wav = "wav"
    opus = "opus"
    ogg = "ogg"
    wma = "wma"
    m4a = "m4a"

class AudioFile(UploadedFile):
    __tablename__ = "audio_files"

    pk_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    file_type: Mapped[AudioFileType] = mapped_column(
        SAEnum(AudioFileType),
        nullable=False
    )

    language_name: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("languages.k_name", ondelete="CASCADE"),
        nullable=False
    )
    language: Mapped[Languages] = relationship(back_populates="audio_files")
    owner: Mapped[User] = relationship(
        "User",
        back_populates="uploaded_audio"
    )

