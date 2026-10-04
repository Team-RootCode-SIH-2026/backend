from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as SUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base

if TYPE_CHECKING:
    from .analyses import Analysis
    from .user import User

class Annotation(Base):
    __tablename__ = "annotations"

    pk_annotation_id: Mapped[uuid.UUID] = mapped_column(
        SUUID(as_uuid=True),
        default=uuid.uuid4,
        primary_key=True
    )
    researcher_id: Mapped[uuid.UUID] = mapped_column(
        SUUID(as_uuid=True),
        ForeignKey("users.pk_id"),
        nullable=False
    )
    analysis_corrected: Mapped[uuid.UUID] = mapped_column(
        SUUID(as_uuid=True),
        ForeignKey("analyses.pk_analysis_id"),
        nullable=False
    )
    corrections: Mapped[dict] = mapped_column(
        JSONB(),
        nullable=False
    )
    researcher: Mapped[User] = relationship(
        "User",
        back_populates="annotations"
    )
    analysis: Mapped[Analysis] = relationship(
        "Analysis",
        back_populates="annotations"
    )


