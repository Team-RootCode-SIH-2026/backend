import enum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.db.database import Base
from models.audio import AudioFile
from models.images import ImageFile
from models.text import TextFile


class EndangermentStatus(str, enum.Enum):
    common = "common"
    potentially_endangered = "potential"
    endangered = "endangered"
    seriously_endangered = "serious"
    moribund = "moribund"
    extinct = "extinct"

class Languages(Base):
    __tablename__ = "languages"

    pk_name: Mapped[str] = mapped_column(                       # Name of the language
        String(255),
        primary_key=True,
    )
    k_code: Mapped[str] = mapped_column(                        # Glottocode (Better than ISO 639-3, iswis)
        String(8),
        unique=True,
        nullable=False
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
        Enum(EndangermentStatus, name="status"),
        nullable=False
    )
    text_files: Mapped[list["TextFile"]] = relationship(back_populates="language")
    audio_files: Mapped[list["AudioFile"]] = relationship(back_populates="language")
    image_files: Mapped[list["ImageFile"]] = relationship(back_populates="language")
