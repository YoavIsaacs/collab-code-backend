from fastapi import APIRouter, Depends
from app.database.dependencies import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.get("/test-connection")
async def test_connection(db: AsyncIOMotorDatabase = Depends(get_database)):
    try:
        server_info = await db.command("ping")
        return {
            "server_info": server_info
        }
    except Exception as e:
        return {
            "status": "Failed to connect to MongoDB",
            "error": str(e)
        }