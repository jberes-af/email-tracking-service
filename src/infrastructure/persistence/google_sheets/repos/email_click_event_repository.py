# /src/infrastructure/persistence/google_sheets/repos/email_click_event_repository.py

from src.application.ports.email_tracking_repository_ports import (
    EmailClickEventRepositoryPort,
)

from src.domain.entities.email_tracking_entities import (
    EmailClickEvent,
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.mappers.email_click_event_row_mapper import (
    EmailClickEventRowMapper,
)

from src.infrastructure.persistence.schemas.email_click_event_columns import (
    EmailClickEventColumns,
)


class GoogleSheetsEmailClickEventRepository(
    GoogleSheetsRepository,
    EmailClickEventRepositoryPort,
):
    TABLE_NAME = "email_click_events"
    ID_COLUMN = EmailClickEventColumns.TRACKING_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: EmailClickEventRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def append_click_event(
            self,
            event: EmailClickEvent,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=EmailClickEventColumns.ORDER,
        )
