# /src/infrastructure/persistence/google_sheets/repos/email_open_event_repository.py

from dataclasses import fields

from src.application.ports.email_tracking_repository_ports import (
    EmailOpenEventRepositoryPort,
)

from src.domain.entities.email_tracking_entities import (
    EmailOpenEvent,
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

from src.infrastructure.persistence.mappers.email_open_event_row_mapper import (
    EmailOpenEventRowMapper,
)

from src.infrastructure.persistence.schemas.email_open_event_columns import (
    EmailOpenEventColumns,
)


class GoogleSheetsEmailOpenEventRepository(
    GoogleSheetsRepository,
    EmailOpenEventRepositoryPort,
):
    TABLE_NAME = "email_open_events"
    ID_COLUMN = EmailOpenEventColumns.TRACKING_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: EmailOpenEventRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def append_open_event(
            self,
            event: EmailOpenEvent,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=EmailOpenEventColumns.ORDER,
        )
