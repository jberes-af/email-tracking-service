# /src/main/compo_root_tracking_repos.py

from dataclasses import dataclass

from src.application.ports.email_tracking_repository_ports import (
    EmailOpenEventRepositoryPort,
    EmailClickEventRepositoryPort,
    EmailMessageRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.mappers.email_message_row_mapper import (
    EmailMessageRowMapper,
)

from src.infrastructure.persistence.mappers.email_open_event_row_mapper import (
    EmailOpenEventRowMapper,
)

from src.infrastructure.persistence.mappers.email_click_event_row_mapper import (
    EmailClickEventRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.email_message_repository import (
    GoogleSheetsEmailMessageRepository,
)

from src.infrastructure.persistence.google_sheets.repos.email_open_event_repository import (
    GoogleSheetsEmailOpenEventRepository,
)

from src.infrastructure.persistence.google_sheets.repos.email_click_event_repository import (
    GoogleSheetsEmailClickEventRepository,
)

from src.main.compo_root_google_sheets_repos.utils_sheets_compo_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)

from src.common.memory import log_memory


@dataclass(frozen=True, slots=True)
class GoogleSheetsEmailTrackingRepositories:
    # email_tracking_repository: EmailTrackingRepositoryPorts
    email_message_repository: EmailMessageRepositoryPort
    email_open_events_repository: EmailOpenEventRepositoryPort
    email_click_events_repository: EmailClickEventRepositoryPort


def build_google_sheets_email_tracking_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsEmailTrackingRepositories:
    log_memory("Before build_google_sheets_query_service")

    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    log_memory("After build_google_sheets_query_service")

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    email_message_repository = GoogleSheetsEmailMessageRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=EmailMessageRowMapper(),
    )

    email_open_repository = GoogleSheetsEmailOpenEventRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=EmailOpenEventRowMapper(),
    )

    email_click_repository = GoogleSheetsEmailClickEventRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=EmailClickEventRowMapper(),
    )

    return GoogleSheetsEmailTrackingRepositories(
        email_message_repository=email_message_repository,
        email_open_events_repository=email_open_repository,
        email_click_events_repository=email_click_repository,
    )
