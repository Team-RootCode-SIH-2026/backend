import uuid
from datetime import UTC, datetime
from functools import partial

from pydantic import BaseModel, Field

from ..models.audio import AudioFileType
from ..models.images import ImageFileType
from ..models.text import TextFileType


# Audio Files
class AudioUpload(BaseModel):

    id: uuid.UUID
    original_filename: str
    type: str
    uploaded_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    size: int
    author_id: uuid.UUID

class AudioRead(BaseModel):
    id: uuid.UUID
    original_filename: str
    category: AudioFileType
    size: int
    created_at: datetime

class AudioList(BaseModel):
    total: int
    items: list[AudioRead]


# Text Files
class TextUpload(BaseModel):

    id: uuid.UUID
    original_filename: str
    type: str
    uploaded_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    size: int
    author_id: uuid.UUID

class TextRead(BaseModel):
    id: uuid.UUID
    original_filename: str
    category: TextFileType
    size: int
    created_at: datetime

class TextList(BaseModel):
    total: int
    items: list[TextRead]


# Image Files
class ImageUpload(BaseModel):

    id: uuid.UUID
    original_filename: str
    type: str
    uploaded_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    size: int
    author_id: uuid.UUID

class ImageRead(BaseModel):
    id: uuid.UUID
    original_filename: str
    category: ImageFileType
    size: int
    created_at: datetime

class ImageList(BaseModel):
    total: int
    items: list[ImageRead]
