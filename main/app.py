from fastapi import FastAPI

from utils.core import get_env_variable
from main.settings import logger, BaseSettings, Settings
from api import news

app = FastAPI(debug=get_env_variable("DEBUG", 0))

app.include_router(news.router)

@app.on_event("startup")
def get_settings() -> BaseSettings:
    """Function to ensure that all required environment variables 
    are loaded
    """
    logger.info("Loading config settings from the environment...")
    return Settings()
