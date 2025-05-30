from fastapi import FastAPI
from app.router import status_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(status_router, prefix="/status", tags=["status"])
    return app


app = create_app()
