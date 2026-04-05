from fastapi import FastAPI
from app.routes import logs
from app.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# include routes
app.include_router(logs.router)

@app.get("/")
def root():
    return {
        "message": "AI Log Monitoring Backend Running 🚀"
    }

