import time
import json
import random
from datetime import datetime
from app.services.redis_client import get_redis_client

services = ["auth", "payment", "orders", "inventory"] 

levels = ["INFO", "WARNING", "ERROR"]

message = [
    "User login successful",
    "Payment processed",
    "Database connection slow",
    "Timeout Error",
    "Invalid request received"
]


def generate_log():
    if random.random() < 0.1:
        response_time = random.uniform(3, 6) # anomaly
    else:
        response_time = random.uniform(0.1, 1.5)

    return {
        "timestamp": datetime.now().isoformat(),
        "service": random.choice(services),
        "level": random.choice(levels),
        "message": random.choice(message),
        "response_time": response_time
    }

if __name__ == "__main__":
    print("🚀 Starting log generator...\n")

    r = get_redis_client()

    while True:
        log = generate_log()
        
        # push to redis queue
        r.lpush("logs_queue", json.dumps(log))

        print("📩 Sent log:", log)

        time.sleep(1)