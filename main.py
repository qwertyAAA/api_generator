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

from api_genenrator.endpoints.route import registered_apps

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

# todo save swagger ui to the local and build a static server to provide swagger ui static files
# todo or just modify "https://cdn.jsdelivr.net/npm/swagger-ui-dist@4" -> "https://petstore.swagger.io"  # fastapi/openapi/docs.py.get_swagger_ui_html lineno get_swagger_ui_html 20-21
if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=9980, workers=1)
