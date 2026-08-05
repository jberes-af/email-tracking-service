# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.emailclickevent_columns import EmailClickEventColumns

from src.domain.entities.patient_entities import EmailClickEvent

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