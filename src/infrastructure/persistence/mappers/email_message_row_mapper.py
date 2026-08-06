# /src/infrastructure/persistence/mappers/email_message_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.email_message_columns import EmailMessageColumns

from src.domain.entities.email_tracking_entities import EmailMessage

from src.infrastructure.persistence.common.utils_parsing import *

class EmailMessageRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> EmailMessage:

        schema = EmailMessageColumns

        return EmailMessage(
            tracking_id=parse_required_text(
                row.get(schema.TRACKING_ID),
                field_name=schema.TRACKING_ID,
            ),
            campaign_name=parse_required_text(
                row.get(schema.CAMPAIGN_NAME),
                field_name=schema.CAMPAIGN_NAME,
            ),
            recipient_email=parse_required_text(
                row.get(schema.RECIPIENT_EMAIL),
                field_name=schema.RECIPIENT_EMAIL,
            ),
            recipient_name=parse_optional_text(
                row.get(schema.RECIPIENT_NAME),
                field_name=schema.RECIPIENT_NAME,
            ),
            subject=parse_required_text(
                row.get(schema.SUBJECT),
                field_name=schema.SUBJECT,
            ),
            sent_at=parse_required_datetime(
                row.get(schema.SENT_AT),
                field_name=schema.SENT_AT,
            ),
        )