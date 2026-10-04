import uuid
from enum import Enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ..db.database import Base


# Does not include the last number in age range
class AgeRange(str, Enum):
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
        SAEnum(AgeRange, values_callable=lambda e: [item.value for item in e]),
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
