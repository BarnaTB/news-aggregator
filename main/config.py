import logging

from pydantic import BaseSettings

from utils.core import get_env_variable
from main.app import app


logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    debug: bool = get_env_variable("DEBUG", 0, required=True)
    news_api_urls: str = get_env_variable("NEWS_API_URLS", required=True)


def get_settings() -> BaseSettings:
    logger.info("Loading config settings from the environment...")
    return Settings()
