from pydantic.v1 import BaseSettings, Field


class Settings(BaseSettings):
    MONGODB_URI: str = Field(..., env="MONGODB_URI")
    MONGODB_NAME: str = Field(default="collaborative_coding_db", env="MONGO_DB_NAME")
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = "../../.env"

settings = Settings()
