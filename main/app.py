from fastapi import FastAPI

from utils.core import get_env_variable


app = FastAPI(debug=get_env_variable("DEBUG", 0))
