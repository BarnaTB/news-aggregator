from http.client import responses
import requests

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from main.settings import settings
from utils.reddit import get_token, make_authorization_url

from utils.core import get_env_variable

router = APIRouter(
    tags=["news"],
    responses={404: {"description": "Not found"}},
    include_in_schema=True
)

@router.get("/")
def homepage():
	text = f"<a href='{make_authorization_url()}'>Authenticate with reddit</a>"
	return HTMLResponse(text)


@router.get("/reddit_callback")
def reddit_callback(request: Request):
    error = request.args.get("error", "")
    if error:
        return "Error: " + error
    code = request.args.get("code")
    print(f">>>>>>>>>>>> {code}")
    token = get_token(code)
    print(f">>>>>>>>>>>> {token}")
    return {"token": token}

@router.get("/news")
def get_news():
    subreddit_url = (
        f"https://www.reddit.com/r/news/"
        f"{settings.reddit_listing}.json"
        f"?limit={settings.reddit_data_limit}"
        f"&t={settings.reddit_timeframe}"
        )
    newsapi_url = (
        "https://newsapi.org/v2/top-headlines?category=general"
        f"&apiKey={settings.newsapi_key}"
        )
    apis = [subreddit_url, newsapi_url]
    environment_set_urls = settings.news_api_urls.split(" ") if len(
    	settings.news_api_urls) != "" else ""
    apis.extend(environment_set_urls) if "" not in environment_set_urls else apis
    
    response = list(map(requests.get, apis))
    responses = [response.json() for response in response]

    for response in responses:
        print(response)
        # print(index)
