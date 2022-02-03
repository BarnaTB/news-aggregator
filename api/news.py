import requests

from fastapi import APIRouter

from main.settings import settings

from utils.core import get_env_variable
from utils.news import format_data

router = APIRouter(
    tags=["news"],
    responses={404: {"description": "Not found"}},
    include_in_schema=True
)

@router.get("/news")
def get_news(query: str = ""):
    subreddit_url = (
        f"{settings.reddit_base_url}/r/news/"
        f"{settings.reddit_listing}.json"
        f"?limit={settings.reddit_data_limit}"
        f"&t={settings.reddit_timeframe}"
        ) if not query else (
            f"{settings.reddit_base_url}/r/news/search"
            f"{settings.reddit_listing}.json?q={query}"
        )
    newsapi_url = (
        f"{settings.newsapi_base_url}/v2/top-headlines?category=general"
        f"&apiKey={settings.newsapi_key}"
        ) if not query else (
            f"{settings.newsapi_base_url}/v2/everything?q={query}"
            f"&apiKey={settings.newsapi_key}"
        )
    apis = [subreddit_url, newsapi_url]
    environment_set_urls = settings.other_api_urls.split(" ") if settings.other_api_urls else ""
    apis.extend(environment_set_urls) if environment_set_urls else apis
    
    responses = list(map(requests.get, apis))
    responses = [response.json() for response in responses]

    formatted_data = format_data(responses)
    response = {
        "success": formatted_data[0],
        "message": formatted_data[1]
    }

    return response["message"]
