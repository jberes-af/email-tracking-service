# /src/presentation/routes.py

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from src.main.composition_root import AppContainer

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "OK"}



@router.get("/click/{tracking_id}")
def click_email(
    tracking_id: str,
    link: str,
):
    ...



@router.get("/open/{tracking_id}")
def open_email(
    tracking_id: str,
    request: Request,
):

    AppContainer.track_email_open_use_case.execute(
        tracking_id=tracking_id,
        ip_address=request.client.host if request.client else None,
        user_agent=request.headers.get("User-Agent"),
    )

    return FileResponse(
        "src/infrastructure/images/transparent.png",
        media_type="image/png",
    )

