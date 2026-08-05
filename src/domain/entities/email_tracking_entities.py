# /src/domain/entities/email_tracking_entities.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class EmailMessage:
    tracking_id: str
    campaign_name: str
    recipient_email: str
    recipient_name: str | None
    subject: str
    sent_at: datetime


@dataclass(frozen=True)
class EmailClickEvent:
    tracking_id: str
    email_message_id: str
    link_name: str
    clicked_at: datetime
    ip_address: str | None
    user_agent: str | None


@dataclass(frozen=True)
class EmailOpenEvent:
    tracking_id: str
    email_message_id: str
    opened_at: datetime
    ip_address: str | None
    user_agent: str | None
