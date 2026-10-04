from enum import Enum
from typing import Annotated
from uuid import uuid4

import filetype

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from ...core.config import settings
from ...core.dependencies import User, get_current_user
