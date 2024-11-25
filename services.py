import os
from mastodon import Mastodon


class ConfigService:
    """Service for validating environmental variables"""
    def validate_config(self) -> bool:
        return all(
            [
                os.getenv("CLIENT_ID"),
                os.getenv("CLIENT_SECRET"),
                os.getenv("ACCESS_TOKEN"),
                os.getenv("API_BASE_URL"),
            ]
        )


class BotService:
    """Service for generating the toots"""
    def prepare_toot_body(self):
        # Here put the logic that will generate the body of the toot
        body = "Hello world!"
        return body


class MastodonService:
    """Service for handling comms with Mastodon"""
    def __init__(self):
        self.mastodon = Mastodon(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            api_base_url=os.getenv("API_BASE_URL"),
        )

    def post(self, body, **kwargs):
        self.mastodon.status_post(body, language="pl", **kwargs)
