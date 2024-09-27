from typing import AsyncGenerator
from app.database.connection import mongodb

async def get_database() -> AsyncGenerator:
    yield mongodb.db
