# /src/application/use_cases/track_email_click_use_case.py

from datetime import datetime
from zoneinfo import ZoneInfo

from src.application.ports.email_tracking_repository_ports import (
    EmailClickEventRepositoryPort,
    EmailMessageRepositoryPort,
)

from src.domain.entities.email_tracking_entities import (
    EmailClickEvent,
)


class TrackEmailClickUseCase:

    def __init__(
        self,
        *,
        messages_repository: EmailMessageRepositoryPort,
        click_events_repository: EmailClickEventRepositoryPort,
    ) -> None:

        self._messages = messages_repository
        self._clicks = click_events_repository

    def execute(
        self,
        *,
        tracking_id: str,
        link_name: str,
        ip_address: str | None,
        user_agent: str | None,
    ) -> None:

        message = self._messages.get_by_tracking_id(
            tracking_id=tracking_id,
        )

        if message is None:
            return

        event = EmailClickEvent(
            tracking_id=tracking_id,
            email_message_id=message.tracking_id,
            link_name=link_name,
            clicked_at=datetime.now(
                ZoneInfo("America/Chicago"),
            ),
            ip_address=ip_address,
            user_agent=user_agent,
        )

        self._clicks.append_click_event(event)
