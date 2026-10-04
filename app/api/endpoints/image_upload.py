from typing import Annotated, cast
from uuid import uuid4

import filetype
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.config import settings
from ...core.dependencies import User, get_current_user, get_db
from ...db.crud import create_image_file_record
from ...models.images import ImageFileType

router = APIRouter(prefix="/uploads/image", tags=["image", "images"])

@router.get("")
async def image_upload(db: Annotated[AsyncSession, Depends(get_db)], user: Annotated[User, Depends(get_current_user)], file: Annotated[UploadFile, File(...)]):
    header = await file.read(4096)
    await file.seek(0)
    type = filetype.guess(header)
    if type is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not determine file type"
        )
    else:
        detected_type = type.extension
    if detected_type not in ImageFileType._value2member_map_:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type {detected_type} is not allowed"
        )
    size = 0;
    filename = f"{uuid4()}"
    full_filename = f"{filename}.{detected_type}"
    dest = settings.UPLOAD_DIR / "images" /full_filename
    try:
        with dest.open("wb") as buffer:
            while chunk := await file.read(settings.CHUNK_SIZE):
                size += len(chunk)
                if size > settings.MAX_UPLOAD_SIZE:
                    dest.unlink(missing_ok=True)
                    raise HTTPException(
                        status_code=status.HTTP_413_CONTENT_TOO_LARGE,
                        detail="File is too large"
                    )
                buffer.write(chunk)
        await create_image_file_record(
            db=db,
            owner_id=user.pk_id,
            original_filename=cast(str, file.filename),
            stored_filename=full_filename,
            category=ImageFileType(detected_type),
            size_bytes=size
        )
    finally:
        await file.close()

