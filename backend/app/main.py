from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest # type: ignore

from app.routes import logs
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME, 
    version=settings.VERSION
    )

# Prometheus metric
REQUEST_COUNT = Counter(
    "request_count",
    "Total number of requests"
)

# include routes
app.include_router(logs.router)

@app.get("/")
def root():
    REQUEST_COUNT.inc()  # increment metric
    return {
        "message": "AI Log Monitoring Backend Running 🚀"
    }


@app.get("/metrics")
def metrics():
    """
    Prometheus will scrape this endpoint
    """
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )