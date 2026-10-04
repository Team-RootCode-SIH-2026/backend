from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Float, String, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base

if TYPE_CHECKING:
    from .annotations import Annotation


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
        JSONB(),
        nullable=False
    )
    confidence_score: Mapped[float] = mapped_column(
        Float(precision=23),
        nullable=False
    )
    analysis_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    annotations: Mapped[list[Annotation]] = relationship(
        "Annotation",
        back_populates="analysis"
    )


