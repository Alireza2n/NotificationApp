import redis
import settings


def redis_connect() -> redis.client.Redis:
    client = redis.Redis.from_url(url=settings.CACHE_BACKEND_URL)
    if client.ping():
        return client


