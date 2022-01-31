from fastapi import FastAPI

from utils.core import get_env_variable
from main.settings import logger, BaseSettings, Settings

app = FastAPI(debug=get_env_variable("DEBUG", 0))

@app.on_event("startup")
def get_settings() -> BaseSettings:
    logger.info("Loading config settings from the environment...")
    return Settings()
