from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str = Field(..., alias="MONGODB_URI")
    MONGO_DB_NAME: str = Field(default="collaborative_coding_db", alias="MONGO_DB_NAME")
    JWT_SECRET_KEY: str = Field(..., alias="JWT_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
