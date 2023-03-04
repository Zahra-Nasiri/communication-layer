from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    user_service_url: str
    book_service_url: str

    class Config:
        env_file = '.env'

@lru_cache()
def get_settings():

    return Settings()