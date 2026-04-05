from fastapi import APIRouter
from app.services.db import SessionLocal
from shared.models.log_model import Log

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/")
def get_logs():
    db = SessionLocal()

    logs = db.query(Log).order_by(Log.id.desc()).limit(50).all()

    result = []

    for log in logs:
        result.append({
            "id": log.id,
            "service": log.service,
            "level": log.level,
            "message": log.message,
            "response_time": log.response_time,
            "is_error": log.is_error,
            "is_anomaly": log.is_anomaly
        })
    
    db.close()
    return result