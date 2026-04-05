from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

from shared.models.log_model import Base

# Kubernetes service name
DATABASE_URL = "postgresql://admin:admin@postgres:5432/logs_db"


def wait_for_db():
    """
    Wait until PostgreSQL is ready 
    """
    while True:
        try:
            engine = create_engine(DATABASE_URL)

            # try connecting
            conn = engine.connect()
            conn.close()

            print("✅ Connected to Postgres")
            
            return engine
        except Exception as e:
            print("⏳ Waiting for Postgres...", e)
            time.sleep(3)

# Create engine after DB is ready
engine = wait_for_db()

# Create session
SessionLocal = sessionmaker(bind=engine)

# Auto-create tables (IMPORTANT)
Base.metadata.create_all(bind=engine)