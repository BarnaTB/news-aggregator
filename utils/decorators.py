from functools import lru_cache, wraps
from datetime import datetime, timedelta

from main.settings import settings


def lru_cache_with_expiry(
    seconds: int=settings.lru_cache_expiry,
    maxsize: int=settings.maximum_cache_size):
    """Function decorator to set an expiry to the cache in memory
    """
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache
