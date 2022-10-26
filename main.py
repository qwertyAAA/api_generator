from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from uvicorn import run

from api_genenrator.common import setup_loguru_uvicorn_logging_intercept
from api_genenrator.common.middlewares.exception_handlers import (
    handle_validation_error,
    handle_http_error,
    handle_server_error
)

from api_genenrator.endpoints.sample_endpoint import registered_apps

app = FastAPI(
    title="API Generator",
    redoc_url=None,  # disable redoc
)

for check_app in registered_apps:
    app.include_router(check_app, prefix="/api/v1")

app.add_exception_handler(RequestValidationError, handle_validation_error)
app.add_exception_handler(HTTPException, handle_http_error)
app.add_exception_handler(Exception, handle_server_error)

setup_loguru_uvicorn_logging_intercept()

if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=9980, workers=1)
