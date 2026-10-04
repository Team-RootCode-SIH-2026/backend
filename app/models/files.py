import uuid
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ..db.database import Base


class UploadedFile(Base):
    __abstract__ = True

    fk_owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.pk_id"),
        nullable=False,
        index=True
    )
    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    size_bytes: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
