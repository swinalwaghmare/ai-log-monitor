from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

from shared.models.log_model import Base

DATABASE_URL = "postgresql://admin:admin@postgres:5432/logs_db"


def wait_for_db():
    while True:
        try:
            engine = create_engine(DATABASE_URL)
            conn = engine.connect()
            conn.close()
            print("✅ Connected to Postgres")
            return engine
        except Exception as e:
            print("⏳ Waiting for Postgres...", e)
            time.sleep(3)


engine = wait_for_db()
SessionLocal = sessionmaker(bind=engine)