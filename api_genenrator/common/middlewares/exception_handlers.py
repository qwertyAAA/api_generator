from typing import Callable

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from starlette.exceptions import HTTPException

from api_genenrator.common import (
    ResponseModel,
    Responses
)
from api_genenrator.common.utils.logger import get_logger

logger = get_logger("exception_handlers")


def handler(func: Callable) -> Callable:
    """
    Wrapper of exception handlers
    catch and handle exceptions when performing handling
    :param func: exception handler
    :return: Callable
    """

    def inner(request: Request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as e:
            logger.exception("An exception occurred while handling server error", e)
            return JSONResponse(
                content=ResponseModel(status=500, msg=Responses[500]["description"]).dict(),
                status_code=500
            )

    return inner


@handler
def handle_validation_error(
        request: Request,
        exception: RequestValidationError
) -> Response:
    """
    RequestValidationError handler
    :param request: FastAPI Request
    :param exception: object of validation errors
    :return: FastAPI Response
    """
    logger.exception(f"request: {request.url} request data validation error: ", exception)
    return JSONResponse(
        content=ResponseModel(
            status=422,
            msg=Responses[422]["description"],
            data={
                "path_params": request.path_params,
                "query_params": dict(request.query_params),
                "detail": str(exception)
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
    logger.exception(f"request: {request.url} failed caused by: ", exception)
    return JSONResponse(
        content=ResponseModel(
            status=exception.status_code,
            msg=Responses.get(exception.status_code, {}).get("description", exception.detail),
            data={
                "headers": dict(request.headers),
                "path_params": request.path_params,
                "query_params": str(request.query_params),
                "detail": exception.detail
            }
        ).dict(),
        status_code=exception.status_code
    )


@handler
def handle_server_error(request: Request, exception: Exception) -> Response:
    """
    Exception handler
    :param request: FastAPI Request
    :param exception: object of Exception
    :return: FastAPI Response
    """
    logger.exception(f"request: {request.url} failed", exception)
    return JSONResponse(
        content=ResponseModel(
            status=500,
            msg=Responses[500]["description"],
            data={
                "headers": dict(request.headers),
                "path_params": request.path_params,
                "query_params": str(request.query_params)
            }).dict(),
        status_code=500
    )
