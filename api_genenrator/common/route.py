from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    Union
)

from fastapi import APIRouter, FastAPI
from fastapi.responses import Response, UJSONResponse

from api_genenrator.common import Responses, ResponseModel


def register(
        app: Union[APIRouter, FastAPI],
        path: str,
        view_func: Callable,
        *,
        description: Optional[str] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        request_method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]] = "GET",
        response_class: Optional[Type[Response]] = UJSONResponse,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = Responses,
        response_model: Optional[Type[Any]] = ResponseModel,
) -> None:
    """
    Register the `view` as a `route` to the `app`
    :param app: object of FastAPI or APIRouter
    :param path: str, `route`
    :param view_func: `view` function or coroutine
    :param description: description of `view`
    :param tags: tags of `view`
    :param request_method: request method
    :param response_class: response class
    :param responses: available responses
    :param response_model: response model
    :return: None
    """
    getattr(app, request_method.lower())(
        path=path,
        response_class=response_class,
        responses=responses,
        response_model=response_model,
        description=description,
        tags=tags
    )(view_func)
