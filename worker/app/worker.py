import json 
import time

from app.services.redis_client import get_redis_client
from app.detectors.error_detector import is_error
from app.detectors.anomaly_detector import is_anomaly
from app.services.db import SessionLocal
from sqlalchemy import text

QUEUE_NAME = "logs_queue"

def process_log(log: dict):
    """
    Process each log
    """
    service = log.get("service")

    is_err = is_error(log)
    is_anom = is_anomaly(log)

    print(type(is_err), is_err)
    print(type(is_anom), is_anom)

    print(f"\n📩 [{service}] Processing log")

    # Rule-based detection
    if is_err:
        print(f"🚨 ERROR DETECTED")
    
    # ML based detection
    if is_anom:
        print(f"⚠️ ANOMALY DETECTED")
    
    # Save to DB
    db = SessionLocal()

    db.execute(
    text("""
        INSERT INTO logs (timestamp, service, level, message, response_time, is_error, is_anomaly)
        VALUES (:timestamp, :service, :level, :message, :response_time, :is_error, :is_anomaly)
    """),
    {
        "timestamp": log.get("timestamp"),
        "service": service,
        "level": log.get("level"),
        "message": log.get("message"),
        "response_time": log.get("response_time"),
        "is_error": is_err,
        "is_anomaly": is_anom,
    }
)

    db.commit()
    db.close()


def start_worker():
    redis_client = get_redis_client()

    print("🚀 Worker started with ML... Waiting for logs...\n")

    while True:
        # BROP = blocking pop (waits until data comes)
        data = redis_client.brpop(QUEUE_NAME)

        if data:
            _, log_json = data
            log = json.loads(log_json)

            process_log(log)

        time.sleep(0.1) # small delay to prevent CPU overuse

if __name__ == "__main__":
    start_worker()