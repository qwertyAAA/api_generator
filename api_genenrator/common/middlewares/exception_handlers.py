from traceback import format_exception_only
from typing import Callable, Any

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi.responses import UJSONResponse

from api_genenrator.common import (
    ResponseModel,
    Responses
)
from api_genenrator.common.utils import get_logger

logger = get_logger("exception_handlers")


def handler(func: Callable) -> Callable:
    """
    Wrapper of exception handlers
    catch and handle exceptions when performing handling
    :param func: exception handler
    :return: Callable
    """

    def inner(request: Request, *args, **kwargs) -> Any:
        try:
            return func(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"An exception occurred while handling server error: "
                         f"{format_exception_only(type(e), e)[0].strip()}")
            return UJSONResponse(
                content=ResponseModel(code=500, msg=Responses[500]["description"]).dict(),
                status_code=500
            )

    return inner


@handler
def handle_validation_error(
        request: Request,
        exception: RequestValidationError
) -> Response:
    """
    Request data validation error handler
    :param request: FastAPI Request
    :param exception: object of validation errors
    :return: FastAPI Response
    """
    logger.error(f"request: {request.url} request data validation error: "
                 f"{format_exception_only(type(exception), exception)[0].strip()}")
    return UJSONResponse(
        content=ResponseModel(
            code=422,
            msg=Responses[422]["description"],
            data={
                "path_params": request.path_params,
                "query_params": dict(request.query_params),
                "error_msg": str(exception)
            }
        ).dict(),
        status_code=422
    )


@handler
def handle_http_error(request: Request, exception: HTTPException) -> Response:
    """
    HTTPException handler
    :param request: FastAPI Request
    :param exception: object of HTTPException
    :return: FastAPI Response
    """
    logger.error(
        f"request: {request.url} failed caused by: "
        f"{format_exception_only(type(exception), exception)[0].strip()}")
    return UJSONResponse(
        content=ResponseModel(
            code=exception.status_code,
            msg=Responses[exception.status_code]["description"],
            data={
                "path_params": request.path_params,
                "query_params": str(request.query_params),
            }
        ).dict(),
        status_code=exception.status_code
    )


@handler
def handle_server_error(request: Request, exception: Exception) -> Response:
    """
    Server Error handler
    :param request: FastAPI Request
    :param exception: object of Exception
    :return: FastAPI Response
    """
    logger.error(
        f"request: {request.url} failed caused by: "
        f"{format_exception_only(type(exception), exception)[0].strip()}")
    return UJSONResponse(
        content=ResponseModel(code=500, msg=Responses[500]["description"], data={
            "path_params": request.path_params,
            "query_params": str(request.query_params),
        }).dict(),
        status_code=500
    )
