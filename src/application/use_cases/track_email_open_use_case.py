# /src/application/use_cases/track_email_open.py

from datetime import datetime
from zoneinfo import ZoneInfo

from src.application.ports.email_tracking_repository_ports import (
    EmailMessageRepositoryPort,
    EmailOpenEventRepositoryPort,
)

from src.domain.entities.email_tracking_entities import (
    EmailOpenEvent,
)


class TrackEmailOpenUseCase:

    def __init__(
        self,
        *,
        messages_repository: EmailMessageRepositoryPort,
        open_events_repository: EmailOpenEventRepositoryPort,
    ) -> None:

        self._messages = messages_repository
        self._opens = open_events_repository

    def execute(
        self,
        *,
        tracking_id: str,
        ip_address: str | None,
        user_agent: str | None,
    ) -> None:

        message = self._messages.get_by_tracking_id(
            tracking_id=tracking_id,
        )

        print("message in use case")
        print(message)
        print()

        if message is None:
            return

        event = EmailOpenEvent(
            tracking_id=tracking_id,
            email_message_id=message.tracking_id,
            opened_at=datetime.now(
                ZoneInfo("America/Chicago"),
            ),
            ip_address=ip_address,
            user_agent=user_agent,
        )

        self._opens.append_open_event(event)

