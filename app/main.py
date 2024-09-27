from fastapi import FastAPI
from app.database.connection import connect_to_mongo, close_mongo_connection
from app.routers.Tests.test_connection import router as test_connection_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()



app = FastAPI(lifespan=lifespan)
app.include_router(test_connection_router)
