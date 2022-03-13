from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Film Manager"
    PROJECT_VERSION = str = "1.0.0"
    SQLALCHEMY_DATABASE_URL: PostgresDsn = "postgresql://user:password@127.0.0.1/app"


settings = Settings()
