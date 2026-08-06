# /src/infrastructure/persistence/google_sheets/repos/email_message_repository.py

from src.application.ports.email_tracking_repository_ports import (
    EmailMessageRepositoryPort,
)

from src.domain.entities.email_tracking_entities import (
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

from src.infrastructure.persistence.mappers.email_message_row_mapper import (
    EmailMessageRowMapper,
)

from src.infrastructure.persistence.schemas.email_message_columns import (
    EmailMessageColumns,
)


class GoogleSheetsEmailMessageRepository(
    GoogleSheetsRepository,
    EmailMessageRepositoryPort,
):
    TABLE_NAME = "email_messages"
    ID_COLUMN = EmailMessageColumns.TRACKING_ID

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

    """
    def list_email_messages(self) -> tuple[EmailMessage, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )
    """

    def get_by_tracking_id(
            self,
            tracking_id: str,
    ) -> EmailMessage:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=tracking_id,
        )

        return self._mapper.to_domain(raw_row)

