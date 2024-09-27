from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

mongodb = MongoDB()

async def connect_to_mongo() -> None:
    mongodb.client = AsyncIOMotorClient(settings.MONGODB_URI)
    mongodb.db = mongodb.client[settings.MONGO_DB_NAME]
    print("Connected to MongoDB.")

async def close_mongo_connection() -> None:
    mongodb.client.close()
    print("Closed MongoDB connection.")
