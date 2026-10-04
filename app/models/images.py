from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .files import UploadedFile
from .languages import Languages

if TYPE_CHECKING:
    from .user import User


class ImageFile(UploadedFile):
    __tablename__ = "image_files"

    pk_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    file_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    language_name: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("languages.k_name"),
        nullable=False
    )
    language: Mapped[Languages] = relationship(
        "Languages",
        back_populates="image_files"
    )
    owner: Mapped[User] = relationship(
        "User",
        back_populates="uploaded_images"
    )


