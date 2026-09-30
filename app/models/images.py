from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.files import UploadedFile
from models.languages import Languages


class ImageFile(UploadedFile):
    __tablename__ = "image_files"

    file_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    language_name: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("languages.pk_name"),
        nullable=False
    )
    language: Mapped["Languages"] = relationship(back_populates="image_files")


