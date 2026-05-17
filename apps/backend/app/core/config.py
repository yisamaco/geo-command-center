from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "GEO Command Center API"
    database_url: str = Field(default="postgresql+psycopg://postgres:postgres@localhost:5432/postgres", alias="DATABASE_URL")


settings = Settings()
