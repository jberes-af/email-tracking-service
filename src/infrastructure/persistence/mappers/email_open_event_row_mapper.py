# /src/infrastructure/persistence/mappers/email_open_event_row_mapper.py

from src.domain.entities.email_tracking_entities import EmailOpenEvent

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.email_open_event_columns import EmailOpenEventColumns

from src.infrastructure.persistence.common.utils_parsing import *

class EmailOpenEventRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> EmailOpenEvent:

        schema = EmailOpenEventColumns

        return EmailOpenEvent(
            tracking_id=parse_required_text(
                row.get(schema.TRACKING_ID),
                field_name=schema.TRACKING_ID,
            ),
            email_message_id=parse_required_text(
                row.get(schema.EMAIL_MESSAGE_ID),
                field_name=schema.EMAIL_MESSAGE_ID,
            ),
            opened_at=parse_optional_datetime(
                row.get(schema.OPENED_AT),
                field_name=schema.OPENED_AT,
            ),
            ip_address=parse_optional_text(
                row.get(schema.IP_ADDRESS),
                field_name=schema.IP_ADDRESS,
            ),
            user_agent=parse_optional_text(
                row.get(schema.USER_AGENT),
                field_name=schema.USER_AGENT,
            ),
        )

    @staticmethod
    def to_row(
            event: EmailOpenEvent,
    ) -> RawRow:
        schema = EmailOpenEventColumns

        return {

            schema.TRACKING_ID:
                event.tracking_id,

            schema.EMAIL_MESSAGE_ID:
                event.email_message_id,

            schema.OPENED_AT:
                event.opened_at.isoformat(),

            schema.IP_ADDRESS:
                event.ip_address or "",

            schema.USER_AGENT:
                event.user_agent or "",
        }