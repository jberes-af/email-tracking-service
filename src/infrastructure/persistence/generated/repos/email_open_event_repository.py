# repository.py.tpl


# AUTO GENERATED

from src.application.ports.email_open_event_repository_port import (
    EmailOpenEventRepositoryPort,
)

from src.domain.entities.email_open_event_entities import (
    EmailOpenEvent,
)

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.mappers.email_open_event.email_open_event_row_mapper import (
    EmailOpenEventRowMapper,
)


from src.infrastructure.persistence.schemas.email_open_event.email_open_event_columns import (
    EmailOpenEventColumns,
)


class GoogleSheetsEmailOpenEventRepository(
    GoogleSheetsRepository,
    EmailOpenEventRepositoryPort,
):

    TABLE_NAME = "email_open_event"
    ID_COLUMN = EmailOpenEventColumns.PATIENT_ID


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

    def list_email_open_events(self) -> tuple[EmailOpenEvent, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> EmailOpenEvent:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
