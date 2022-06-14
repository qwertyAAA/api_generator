"""logger(loguru) utils"""

import logging
from pathlib import Path

from loguru import logger

from api_genenrator.common import settings


def get_logger(logger_name: str, **kwargs) -> logger:
    """
    get a bound logger
    :param logger_name: name of logger
    :param kwargs: other kwargs for logger.add exclude `sink`, `rotation`, `filter`
    :return: logger
    """
    if "sink" in kwargs:
        del kwargs["sink"]
        logger.warning("`sink` argument is not supported")

    if "rotation" in kwargs:
        del kwargs["rotation"]
        logger.warning("`rotation` argument is not supported")

    if "filter" in kwargs:
        del kwargs["filter"]
        logger.warning("`filter` argument is not supported")

    logger.add(
        Path(settings.log_dir, logger_name),
        rotation=settings.log_rotation,
        filter=lambda record: record["extra"].get("logger_name") == logger_name,
        **kwargs
    )
    return logger.bind(logger_name=logger_name)


class InterceptHandler(logging.Handler):
    """The handler to intercept standard logging messages and toward Loguru sinks"""

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_loguru_uvicorn_logging_intercept() -> None:
    """
    setup loguru as uvicorn logging interceptor
    :return: None
    """
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.getLevelName("INFO"))

    for logger_name in ("uvicorn.error", "uvicorn.asgi", "uvicorn.access"):
        mod_logger = logging.getLogger(logger_name)
        mod_logger.handlers = [InterceptHandler(level=logging.getLevelName("INFO"))]
        mod_logger.propagate = False
