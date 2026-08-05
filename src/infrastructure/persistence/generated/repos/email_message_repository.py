# repository.py.tpl


# AUTO GENERATED

from src.application.ports.email_message_repository_port import (
    EmailMessageRepositoryPort,
)

from src.domain.entities.email_message_entities import (
    EmailMessage,
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

from src.infrastructure.persistence.mappers.email_message.email_message_row_mapper import (
    EmailMessageRowMapper,
)


from src.infrastructure.persistence.schemas.email_message.email_message_columns import (
    EmailMessageColumns,
)


class GoogleSheetsEmailMessageRepository(
    GoogleSheetsRepository,
    EmailMessageRepositoryPort,
):

    TABLE_NAME = "email_message"
    ID_COLUMN = EmailMessageColumns.PATIENT_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: EmailMessageRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_email_messages(self) -> tuple[EmailMessage, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> EmailMessage:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
