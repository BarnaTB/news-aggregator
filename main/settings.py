import logging

from pydantic import BaseSettings

from utils.core import get_env_variable


logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    debug: bool = get_env_variable("DEBUG", 1, required=True)
    news_api_urls: str = get_env_variable("NEWS_API_URLS", default="")
    newsapi_key: str = get_env_variable("NEWSAPI_KEY", required=True)
    reddit_app_client_id: str = get_env_variable(
        "REDDIT_APP_CLIENT_ID", required=True)
    reddit_app_secret: str = get_env_variable(
        "REDDIT_APP_SECRET", required=True)
    reddit_app_redirect_uri: str = get_env_variable(
        "REDDIT_APP_REDIRECT_URI", required=True)
    reddit_data_limit: str = get_env_variable(
        "REDDIT_DATA_LIMIT", required=True)
    reddit_listing: str = get_env_variable(
        "REDDIT_LISTING", default="new", required=False)
    reddit_timeframe: str = get_env_variable(
        "REDDIT_TIMEFRAME", default="all", required=True)

settings = Settings()
