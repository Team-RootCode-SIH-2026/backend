from datetime import UTC, datetime
from functools import partial

from pydantic import BaseModel, Field


class AudioUpload(BaseModel):
    uploaded_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    size: int
    author_id: str

