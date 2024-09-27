from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_NAME: str = "collaborative_coding_db"
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

