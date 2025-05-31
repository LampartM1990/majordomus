from fastapi import FastAPI
from app.router import status_router
from app.app_config import Config
from app.services.db.init_db import get_db_lifespan


def create_app() -> FastAPI:
    config = Config()
    app = FastAPI(
        title="Majordomus API",
        description="API for Majordomus, a home automation system",
        version="0.0.0",
        debug=config.debug,
        lifespan=get_db_lifespan(config)
    )
    app.include_router(status_router, prefix="/status", tags=["status"])
    return app


app = create_app()
