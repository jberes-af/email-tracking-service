# repository.py.tpl


# AUTO GENERATED

from src.application.ports.email_click_event_repository_port import (
    EmailClickEventRepositoryPort,
)

from src.domain.entities.email_click_event_entities import (
    EmailClickEvent,
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

from src.infrastructure.persistence.mappers.email_click_event.email_click_event_row_mapper import (
    EmailClickEventRowMapper,
)


from src.infrastructure.persistence.schemas.email_click_event.email_click_event_columns import (
    EmailClickEventColumns,
)


class GoogleSheetsEmailClickEventRepository(
    GoogleSheetsRepository,
    EmailClickEventRepositoryPort,
):

    TABLE_NAME = "email_click_event"
    ID_COLUMN = EmailClickEventColumns.PATIENT_ID


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

    def list_email_click_events(self) -> tuple[EmailClickEvent, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> EmailClickEvent:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
