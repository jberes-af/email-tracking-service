# /src/application/use_cases/track_email_open.py

from datetime import datetime
from zoneinfo import ZoneInfo

from src.domain.entities.email_tracking_entities import EmailOpenEvent

from src.application.ports.email_tracking_repository_port import (
    EmailTrackingRepositoryPorts,
)


class TrackEmailOpenUseCase:

    def __init__(
            self,
            repository: EmailTrackingRepositoryPorts,
    ) -> None:
        self._repository = repository

    def execute(
            self,
            *,
            tracking_id: str,
            ip_address: str | None,
            user_agent: str | None,
    ) -> None:
        """
        Records that an email has been opened.
        """

        event = EmailOpenEvent(
            tracking_id=tracking_id,
            opened_at=datetime.now(
                ZoneInfo("America/Chicago")
            ),
            ip_address=ip_address,
            user_agent=user_agent,
        )

        self._repository.record_open(
            event=event,
        )
