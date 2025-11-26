from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 9000
    API_RELOAD: bool = False
    API_PROXY_HEADERS: bool = True

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()
