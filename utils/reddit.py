import requests
import requests.auth
import urllib

from uuid import uuid4

from main.settings import settings


def make_authorization_url() -> str:
	"""Helper function to generate an authorization URL for reddit
    """
	# Generate a random string for the state parameter
	# Save it for use later to prevent xsrf attacks
	state = str(uuid4())
	params = {
		"client_id": settings.reddit_app_client_id,
		"response_type": "code",
		"state": state,
		"redirect_uri": settings.reddit_app_redirect_uri,
		"duration": "temporary",
		"scope": "identity"
		}
	params = urllib.parse.urlencode(params)
	url = f"https://ssl.reddit.com/api/v1/authorize?{params}"
	return url


def get_token(code: str) -> str:
	"""Helper function to return an access token from reddit

	Args:
		code[str]: verification code from OAuth 
	"""
	client_auth = requests.auth.HTTPBasicAuth(
		settings.reddit_app_client_id,
		settings.reddit_app_secret)
	post_data = {
		"grant_type": "authorization_code",
		"code": code,
		"redirect_uri": settings.reddit_app_redirect_uri
		}
	response = requests.post(
		"https://ssl.reddit.com/api/v1/access_token",
		auth=client_auth,
		data=post_data)
	json_response = response.json()
	return json_response["access_token"]
