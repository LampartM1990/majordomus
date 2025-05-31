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


class ProjectDB:
    user = validate_env_var("MONGO_ROOT_USER")
    password = validate_env_var("MONGO_ROOT_PASS")
    port = validate_env_var("MONGO_PORT")
    host = 'mongo'


class Config:
    environment = validate_env_var("ENVIRONMENT")
    debug = validate_env_var("DEBUG").lower() == "true"
    path = ProjectPaths()
    api = ApiConfig()
    db = ProjectDB()
