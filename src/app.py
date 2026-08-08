# /src/app.py

from fastapi import FastAPI

from src.common.memory import log_memory
from src.main.composition_root import build_app_container
from src.presentation.api.routes import router

app = FastAPI(
    title="Email Tracking Service",
)

app.state.container = build_app_container()

app.include_router(router)


@app.on_event("startup")
async def startup_event() -> None:
    log_memory("Startup")
