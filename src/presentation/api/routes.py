# /src/presentation/api/routes.py

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from pathlib import Path

import logging

logger = logging.getLogger(__name__)

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
    print("OPEN ROUTE HIT")
    print()

    container = request.app.state.container

    print("container")
    print(container)
    print(container.track_open_event_use_case)
    print()

    container.track_open_event_use_case.execute(
        tracking_id=tracking_id,
        ip_address=request.client.host if request.client else None,
        user_agent=request.headers.get("User-Agent"),
    )

    return FileResponse(
        container.tracking_pixel_path,
        media_type="image/png",
    )


"""
@router.get("/open/{tracking_id}")
def open_email(
        tracking_id: str,
        request: Request,
):
    print("OPEN ROUTE HIT")

    container = getattr(request.app.state, "container", None)

    ip_address = (
        request.client.host
        if request.client
        else None
    )

    user_agent = request.headers.get("User-Agent")

    if container is not None:

        try:
            container.track_open_event_use_case.execute(
                tracking_id=tracking_id,
                ip_address=ip_address,
                user_agent=user_agent,
            )

        except Exception:
            logger.exception(
                "Unable to record email open."
            )
        else:
            logger.info(
                "Email opened: %s",
                tracking_id,
            )

    print()
    print('image path')
    print(container.tracking_pixel_path)
    print()

    return FileResponse(
        container.tracking_pixel_path,
        media_type="image/png",
    )
"""
