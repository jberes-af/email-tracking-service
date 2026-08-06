# /src/infrastructure/persistence/mappers/email_click_event_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.email_click_event_columns import EmailClickEventColumns

from src.domain.entities.email_tracking_entities import EmailClickEvent

from src.infrastructure.persistence.common.utils_parsing import *


class EmailClickEventRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> EmailClickEvent:
        schema = EmailClickEventColumns

        return EmailClickEvent(
            tracking_id=parse_required_text(
                row.get(schema.TRACKING_ID),
                field_name=schema.TRACKING_ID,
            ),
            email_message_id=parse_required_text(
                row.get(schema.EMAIL_MESSAGE_ID),
                field_name=schema.EMAIL_MESSAGE_ID,
            ),
            link_name=parse_required_text(
                row.get(schema.LINK_NAME),
                field_name=schema.LINK_NAME,
            ),
            clicked_at=parse_required_datetime(
                row.get(schema.CLICKED_AT),
                field_name=schema.CLICKED_AT,
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
            event: EmailClickEvent,
    ) -> RawRow:
        schema = EmailClickEventColumns

        return {

            schema.TRACKING_ID:
                event.tracking_id,

            schema.EMAIL_MESSAGE_ID:
                event.email_message_id,

            schema.LINK_NAME:
                event.link_name or "",

            schema.CLICKED_AT:
                event.clicked_at.isoformat(),

            schema.IP_ADDRESS:
                event.ip_address or "",

            schema.USER_AGENT:
                event.user_agent or "",
        }
