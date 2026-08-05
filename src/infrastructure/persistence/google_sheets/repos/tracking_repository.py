# /src/infrastructure/persistence/google_sheets/repos/tracking_repository.py

from src.domain.entities.email_tracking_entities import (
    EmailOpenEvent,
)

from src.application.ports.email_tracking_repository_port import (
    EmailTrackingRepositoryPorts,
)


class GoogleSheetEmailTrackingRepository(
    EmailTrackingRepositoryPorts,
):

    def record_open(
            self,
            event: EmailOpenEvent,
    ) -> None:
        self._worksheet.append_row(
            [
                event.tracking_id,
                event.opened_at.isoformat(),
                event.ip_address,
                event.user_agent,
            ]
        )
