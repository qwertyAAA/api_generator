#  Copyright (c) 2022, Hyve Solutions. All rights reserved

from typing import Optional

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


class ResponseModel(BaseModel):
    """
    Response model
    """
    code: int = Field(..., description="status code")
    msg: str = Field(..., description="response message")
    data: Optional[dict] = Field({}, description="response data")


responses = {
    200: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "OK"
    },
    201: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Created"
    },
    205: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Reset Content"
    },
    400: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Bad Request"
    },
    401: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Unauthorized"
    },
    403: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Forbidden"
    },
    404: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Not Found"
    },
    405: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Method Not Allowed"
    },
    409: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Conflict"
    },
    422: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Unprocessable Entity"
    },
    500: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Internal Server Error"
    },
}
