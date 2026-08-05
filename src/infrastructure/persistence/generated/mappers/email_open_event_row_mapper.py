# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.emailopenevent_columns import EmailOpenEventColumns

from src.domain.entities.patient_entities import EmailOpenEvent

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
            opened_at=parse_required_datetime(
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