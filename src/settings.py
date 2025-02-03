from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database_connection: str = Field(..., env="DATABASE_CONNECTION")

    class Config:
        env_prefix = ""
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
