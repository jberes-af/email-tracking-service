# /src/application/services/tracking_service.py

class TrackingService:

    def build_tracking_url(
        self,
        tracking_id: str,
    ) -> str:

        return (
            f"https://email.alertahome.com/open/{tracking_id}"
        )

    def build_click_url(
        self,
        tracking_id: str,
        link_name: str,
    ) -> str:

        return (
            f"https://email.alertahome.com/click/{tracking_id}?link={link_name}"
        )
