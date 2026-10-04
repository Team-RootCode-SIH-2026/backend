from __future__ import annotations

import enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base

if TYPE_CHECKING:
    from .audio import AudioFile
    from .images import ImageFile
    from .text import TextFile


class EndangermentStatus(str, enum.Enum):
    common = "common"
    potentially_endangered = "potential"
    endangered = "endangered"
    seriously_endangered = "serious"
    moribund = "moribund"
    extinct = "extinct"

class Languages(Base):
    __tablename__ = "languages"

    k_name: Mapped[str] = mapped_column(                       # Name of the language
        String(255),
        unique=True,
        nullable=False
    )
    pk_code: Mapped[str] = mapped_column(                        # Glottocode (Better than ISO 639-3, iswis)
        String(8),
        primary_key=True,
    )
    family: Mapped[str] = mapped_column(                        # Family of language
        String(255),
        nullable=False
    )
    region: Mapped[str] = mapped_column(                        # Geographic region with most number of speakers
        String(255),
        nullable=False
    )
    status: Mapped[EndangermentStatus] = mapped_column(         # Endangerment status
        Enum(EndangermentStatus, name="status", values_callable=lambda e: [item.value for item in e]),
        nullable=False
    )
    text_files: Mapped[list[TextFile]] = relationship(
        "TextFile",
        back_populates="language"
    )
    audio_files: Mapped[list[AudioFile]] = relationship(
        "AudioFile",
        back_populates="language"
    )
    image_files: Mapped[list[ImageFile]] = relationship(
        "ImageFile",
        back_populates="language"
    )
