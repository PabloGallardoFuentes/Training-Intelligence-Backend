from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.repositories.db import init_db
from src.routes.sessions import router as sessions_router
from src.routes.weekly_load import router as weekly_load_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown
    # close_db()

app = FastAPI(title="Training Intelligence Backend")

app.include_router(sessions_router)
app.include_router(weekly_load_router)