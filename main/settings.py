import logging

from pydantic import BaseSettings

from utils.core import get_env_variable


logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    other_api_urls: str = get_env_variable("NEWS_API_URLS", default="")
    other_api_query_keys: str = get_env_variable("OTHER_API_QUERY_KEYS", default="")
    newsapi_key: str = get_env_variable("NEWSAPI_KEY", required=True)
    reddit_data_limit: str = get_env_variable(
        "REDDIT_DATA_LIMIT", required=True)
    reddit_listing: str = get_env_variable(
        "REDDIT_LISTING", default="new", required=False)
    reddit_timeframe: str = get_env_variable(
        "REDDIT_TIMEFRAME", default="all", required=True)
    reddit_base_url: str = get_env_variable("REDDIT_BASE_URL", required=False)
    newsapi_base_url: str = get_env_variable("NEWSAPI_BASE_URL", required=False)

settings = Settings()
