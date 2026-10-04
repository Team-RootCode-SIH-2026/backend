from watchfiles.run import detect_target_type
from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from cachetools import TTLCache, cached
import filetype
from uuid import uuid4

from ...core.dependencies import get_current_user
from ...core.config import settings

router = APIRouter(prefix="/uploads/audio", tags=["audio"])

cache = TTLCache(maxsize=100, ttl=600)

allowed_file_types = {
    "mp3",
    "wav",
    "opus",
    "ogg",
    "wma",
    "m4a"
}

@router.get("")
async def audio_upload(file: UploadFile = File(...), user = Depends(dependency=get_current_user)):
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
    if detected_type not in allowed_file_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type {detected_type} is not allowed",
        )
    size = 0
    filename = f"{uuid4()}"
    full_file_name = f"{filename}.{detected_type}"
    dest = settings.UPLOAD_DIR / full_file_name
    try:
        with dest.open("wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)
                if size > 10 * 1024 * 1024:
                    raise HTTPException(
                        status_code=status.HTTP_413_CONTENT_TOO_LARGE,
                        detail="File is too large"
                    )
                buffer.write(chunk)
    finally:
        await file.close()
            

