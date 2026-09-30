import uuid

from sqlalchemy import Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.database import Base


# Does not include the last number in age range
class AgeRange(Enum, str):
    child = "0-18"
    young_adult = "18-30"
    middle_age = "30-55"
    old = "55+"

class Speakers(Base):
    __tablename__ = "speakers"

    pk_speaker_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    age_range: Mapped[AgeRange] = mapped_column(
        AgeRange,
        nullable=False
    )
    dialect: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    community: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
