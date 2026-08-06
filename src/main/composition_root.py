# /src/main/composition_root.py

from dataclasses import dataclass
from pathlib import Path

# --- APPLICATION DTOs


# --- APPLICATION PORTS

# from src.application.ports.m365_email_ports import MailSenderPort

# --- APPLICATION USE CASES

from src.application.use_cases.track_email_open_use_case import (
    TrackEmailOpenUseCase,
)

from src.application.use_cases.track_email_click_use_case import (
    TrackEmailClickUseCase,
)

# --- INFRASTRUCTURE CONFIGURATION

from src.infrastructure.config.app_config_loader import (
    AppConfigLoader,
)
from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.secret_provider import (
    EnvSecretProvider,
    StreamlitSecretProvider,
    FallbackSecretProvider,
    SecretProvider,
)

from src.infrastructure.config.settings_loader import (
    load_settings,
)

from src.infrastructure.config.settings_model import (
    Settings,
)

# --- REPOSITORY BUILDERS

from src.main.compo_root_google_sheets_repos.compo_root_tracking_repos import (
    GoogleSheetsEmailTrackingRepositories,
    build_google_sheets_email_tracking_repositories,
)

# --- INTERFACE ADAPTERS

# from src.interface_adapters.presenters.patient.patient_overview_presenter import (
#    PatientOverviewPresenter,)

# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service

import logging

IMAGE_PATH = (
        Path(__file__)
        .parents[2]
        / "src"
        / "infrastructure"
        / "images"
        / "transparent.png"
)


@dataclass(frozen=True, slots=True)
class AppContainer:
    # settings: Settings
    # app_config: AppRuntimeConfig
    # patient_admin_repo: PatientRepositoryPort
    tracking_pixel_path: Path
    track_open_event_use_case: TrackEmailOpenUseCase
    track_click_event_use_case: TrackEmailClickUseCase


def _resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_secret_provider(
        *,
        project_root: Path,
) -> SecretProvider:
    secret_provider = FallbackSecretProvider(
        StreamlitSecretProvider(),
        EnvSecretProvider(
            env_path=project_root / ".env",
            require_env_file=False,
        ),
    )
    return secret_provider


def load_runtime_config() -> tuple[Settings, AppRuntimeConfig]:
    project_root = _resolve_project_root()

    logging.info("Project root resolved: %s", project_root)

    secret_provider = _build_secret_provider(
        project_root=project_root,
    )

    settings = load_settings(
        project_root=project_root,
        secret_provider=secret_provider,
    )

    app_config = AppConfigLoader.load_from_json(
        settings.config_path,
        project_root=project_root,
    )

    return settings, app_config


def build_app_container() -> AppContainer:
    runtime_config: tuple[Settings, AppRuntimeConfig] = load_runtime_config()
    settings: Settings = runtime_config[0]
    app_config: AppRuntimeConfig = runtime_config[1]

    # --- ASSIGN REPOSITORIES: PATIENT

    email_tracking_repos: GoogleSheetsEmailTrackingRepositories = (
        build_google_sheets_email_tracking_repositories(
            settings=settings,
            app_config=app_config,
        ))

    # --- ASSIGN USE CASES

    track_open_use_case = TrackEmailOpenUseCase(
        messages_repository=email_tracking_repos.email_message_repository,
        open_events_repository=email_tracking_repos.email_open_events_repository,
    )

    track_click_use_case = TrackEmailClickUseCase(
        messages_repository=email_tracking_repos.email_message_repository,
        click_events_repository=email_tracking_repos.email_click_events_repository,
    )

    # --- ASSIGN PRESENTERS

    return AppContainer(
        track_open_event_use_case=track_open_use_case,
        track_click_event_use_case=track_click_use_case,
        tracking_pixel_path=IMAGE_PATH,
        # tracking_pixel_path=Path("src/infrastructure/images/transparent.png")
    )
