from pathlib import Path
from typing import Any
import os


def validate_env_var(var_name) -> Any:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"{var_name} environment variable must be set.")
    return value


class ApiConfig:
    PORT = int(validate_env_var("API_PORT"))


class ProjectPaths:
    root = Path(__file__).parent.parent
    app = root / "app"


class Config:
    environment = validate_env_var("ENVIRONMENT")
    path = ProjectPaths()
    api = ApiConfig()
