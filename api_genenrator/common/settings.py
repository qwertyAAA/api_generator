import os
from datetime import timedelta, time
from pathlib import Path
from typing import Optional, List, Union, Callable, Any

from pydantic import (
    BaseSettings
)


class Settings(BaseSettings):
    """settings class"""

    # prod env, turn off openapi
    # openapi_url: Optional[str] = ""
    # dev env, turn on openapi
    openapi_url: Optional[str] = "/openapi.json"

    # CORS origins
    origins: Optional[List[str]] = ["*"]

    # base dir
    base_dir: Path = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # log dir
    log_dir: Path = Path(base_dir, "logs")

    # log rotation
    log_rotation: Union[int, timedelta, time, str, Callable] = 10485760  # 10MiB

    # timezone
    timezone: str = "UTC"

    # singleton instance
    _instance: Optional[Any] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


settings = Settings(
    _env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "settings.conf"),
    _env_file_encoding="utf-8"
)
