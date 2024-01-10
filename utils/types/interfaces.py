from typing import TypedDict, Union
from enum import Enum


class ResponseType(Enum):
    success = {"code": "SUCCESSFULLY COMPLETED", "message": "", "error": ""}
    error = {"code": "ERROR ENCOUNTERED", "message": "", "error": ""}
