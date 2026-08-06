# /src/infrastructure/persistence/schemas/email_open_event_columns.py

class EmailOpenEventColumns:
    TRACKING_ID: str = "tracking_id"
    EMAIL_MESSAGE_ID: str = "email_message_id"
    OPENED_AT: str = "opened_at"
    IP_ADDRESS: str = "ip_address"
    USER_AGENT: str = "user_agent"

    ORDER = (
        TRACKING_ID,
        EMAIL_MESSAGE_ID,
        OPENED_AT,
        IP_ADDRESS,
        USER_AGENT,
    )

