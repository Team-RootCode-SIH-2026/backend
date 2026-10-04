from typing import Annotated, cast
from uuid import uuid4

import filetype
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.config import settings
from ...core.dependencies import User, get_current_user
from ...db.crud import create_text_file_record
from ...db.database import get_db
from ...models.text import TextFileType

router = APIRouter(prefix="/uploads/text", tags=["text"])

@router.get("")
async def text_upload(db: Annotated[AsyncSession, get_db()],user: Annotated[User, Depends(get_current_user)], file: Annotated[UploadFile, File(...)]):
    header = await file.read(4096)
    await file.seek(0)
    type = filetype.guess(header)
    if type is None:
        if file.content_type == "text/plain":
            detected_type = "txt"
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Could not determine file type"
            )
    else:
        detected_type = type.extension
    
    if type not in TextFileType._value2member_map_:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type {detected_type} is not allowed"
        )
    size = 0
    filename = f"{uuid4()}"
    full_file_name = f"{filename}.{detected_type}"
    dest = settings.UPLOAD_DIR / "text" / full_file_name
    try:
        with dest.open("wb") as buffer:
            while chunk := await file.read(settings.CHUNK_SIZE):
                size += len(chunk)
                if size > settings.MAX_UPLOAD_SIZE:
                    raise HTTPException(
                        status_code=status.HTTP_413_CONTENT_TOO_LARGE,
                        detail="File is too large"
                    )
                buffer.write(chunk)
        await create_text_file_record(
            db=db,
            owner_id=user.pk_id,
            original_filename=cast(str, file.filename),
            stored_filename=full_file_name,
            category=TextFileType(detected_type),
            size_bytes=size
        )
    finally:
        await file.close()
