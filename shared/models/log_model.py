from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    service = Column(String)
    level = Column(String)
    message = Column(String)
    response_time = Column(Float)
    is_error = Column(Boolean)
    is_anomaly = Column(Boolean)