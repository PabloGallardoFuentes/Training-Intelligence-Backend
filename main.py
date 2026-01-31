from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session

from src.repositories.orm.user import UserORM
from src.repositories.db import SessionLocal, get_db, init_db
from src.routes.sessions import router as sessions_router
from src.routes.weekly_load import router as weekly_load_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    # Load one user
    with SessionLocal() as db:
        user = db.query(UserORM).filter(UserORM.id == 1).first()
        if not user:
            user = UserORM(id=1)
            db.add(user)
            db.commit()
    yield
    # Shutdown
    # close_db()

app = FastAPI(title="Training Intelligence Backend", lifespan=lifespan)

app.include_router(sessions_router)
app.include_router(weekly_load_router)