# /src/application/ports/email_tracking_repository_port.py

from abc import ABC, abstractmethod

from src.domain.entities.email_tracking_entities import (
    EmailClickEvent,
    EmailOpenEvent,
)


class EmailTrackingRepositoryPorts(ABC):

    @abstractmethod
    def record_open(
            self,
            event: EmailOpenEvent,
    ) -> None:
        ...

    @abstractmethod
    def record_click(
            self,
            event: EmailClickEvent,
    ) -> None:
        ...
