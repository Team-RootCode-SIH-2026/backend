from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.files import UploadedFile
from models.languages import Languages


class TextFile(UploadedFile):
    __tablename__ = "text_files"

    file_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    language_name: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("languages.pk_name")
    )
    language: Mapped["Languages"] = relationship(back_populates="text_files")
