from motor.motor_asyncio import AsyncIOMotorClient
from app.models.demo import Task
from beanie import init_beanie

client: AsyncIOMotorClient


async def connect_to_mongo(config):
    global client
    password = config.db.password
    username = config.db.user
    host = config.db.host
    port = config.db.port

    client = AsyncIOMotorClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
    await init_beanie(
        database=client.majordomus,
        document_models=[Task],
    )


async def check_mongo_connection():
    return await client.admin.command("ping")


async def close_mongo_connection():
    client.close()
