import os
from typing import Any, Dict

import requests


class Client:
    """Telegram client."""

    def __init__(self, token: str):
        self.token = token

    @staticmethod
    def from_envorinment() -> "Client":
        """Create a client from the TELEGRAM_TOKEN environment variable."""

        if "TELEGRAM_TOKEN" not in os.environ:
            raise Exception(
                "TELEGRAM_TOKEN environment variable not found. "
                "Please set it to your Telegram API token."
            )

        return Client(token=os.environ['TELEGRAM_TOKEN'])

    def send(self, msg: str, chat_id: str) -> Dict[str, Any]:
        """Send a message to a chat."""

        params = {
            'chat_id': chat_id,
            'text': msg
        }

        r = requests.get(
            f'https://api.telegram.org/{self.token}/sendMessage',
            params=params
        )

        r.raise_for_status()
        
        return r.json()
