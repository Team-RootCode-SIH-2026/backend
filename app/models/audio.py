from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.db.database import Base
from models.languages import Languages


class AudioFile(Base):
    __tablename__ = "audio_files"

    file_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    language_name: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("languages.pk_name", ondelete="CASCADE"),
        nullable=False
    )
    language: Mapped["Languages"] = relationship(back_populates="audio_files")

