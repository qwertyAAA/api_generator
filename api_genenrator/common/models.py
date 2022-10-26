from typing import Optional

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    """
    Response model
    """
    status: Optional[int] = Field(200, description="status code")
    msg: Optional[str] = Field("OK", description="response message")
    data: Optional[dict] = Field({}, description="response data")


Responses = {
    200: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "OK"
    },
    201: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Created"
    },
    400: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Bad Request"
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
    422: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Unprocessable Entity"
    },
    500: {
        "model": ResponseModel,
        "content": {"application/json": {}}, "description": "Internal Server Error"
    },
}
