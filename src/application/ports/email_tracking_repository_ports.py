# /src/application/ports/email_tracking_repository_ports.py

from abc import ABC, abstractmethod

from src.domain.entities.email_tracking_entities import (
    EmailMessage,
    EmailClickEvent,
    EmailOpenEvent,
)


class EmailOpenEventRepositoryPort(ABC):

    @abstractmethod
    def append_open_event(
            self,
            event: EmailOpenEvent,
    ) -> None:
        ...


class EmailMessageRepositoryPort(ABC):

    @abstractmethod
    def get_by_tracking_id(
            self,
            tracking_id: str,
    ) -> EmailMessage | None:
        """Returns the message or None if not found."""
        ...


class EmailClickEventRepositoryPort(ABC):

    @abstractmethod
    def append_click_event(
            self,
            event: EmailClickEvent,
    ) -> None:
        ...
