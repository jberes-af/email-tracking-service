# /src/app.py

from fastapi import FastAPI

from src.presentation.api.routes import router

app = FastAPI(
    title="Email Tracking Service",
)

app.include_router(router)