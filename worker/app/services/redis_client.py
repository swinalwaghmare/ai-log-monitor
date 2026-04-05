import redis # type: ignore
import time

def get_redis_client():
    while True:
        try:
            client = redis.Redis(
                host="redis",
                port=6379,
                decode_responses=True
            )

            # test connection
            client.ping()

            print("✅ Connected to Redis")
            return client

        except redis.exceptions.ConnectionError:
            print("⏳ Waiting for Redis to be ready...")
            time.sleep(3)
    # return redis.Redis(host="redis", port=6379, decode_responses=True)