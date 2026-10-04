from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base

if TYPE_CHECKING:
    from .annotations import Annotation
    from .audio import AudioFile
    from .images import ImageFile
    from .text import TextFile


class User(Base):
    __tablename__ = "users"

    pk_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    k_email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    k_username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=False,
        nullable=False
    )
    hashed_pwd: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    uploaded_audio: Mapped[list[AudioFile]] = relationship(
        "AudioFile",
        back_populates="owner",
    )
    uploaded_images: Mapped[list[ImageFile]] = relationship(
        "ImageFile",
        back_populates="owner"
    )
    uploaded_text: Mapped[list[TextFile]] = relationship(
        "TextFile",
        back_populates="owner"
    )
    annotations: Mapped[list[Annotation]] = relationship(
        "Annotation",
        back_populates="researcher"
    )
    

