import enum
import uuid
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Enum, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    pk_analysis_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    subject_type: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    pipeline: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    model_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    model_version: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    analysis_result: Mapped[dict] = mapped_column(
        JSONB()
    )

