from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_DATABASE: str
    MYSQL_PORT: int = 3306

    DATABASE_URL: str = ""

    @model_validator(mode="after")
    def assemble_database_url(self) -> "Settings":
        self.DATABASE_URL = (
            f"mysql+asyncmy://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )
        return self

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
