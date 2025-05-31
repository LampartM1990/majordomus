from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services.db.connection import connect_to_mongo, close_mongo_connection


def get_db_lifespan(config):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await connect_to_mongo(config)
        yield
        await close_mongo_connection()
    return lifespan
