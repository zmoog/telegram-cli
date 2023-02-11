import os
from typing import Any, Dict

import requests


class Client:
    """Telegram client."""

    def __init__(self, token: str, debug: bool = False):
        self.token = token
        self.debug = debug

    @staticmethod
    def from_envorinment(debug: bool = False) -> "Client":
        """Create a client from the TELEGRAM_TOKEN environment variable."""

        if "TELEGRAM_TOKEN" not in os.environ:
            raise Exception(
                "TELEGRAM_TOKEN environment variable not found. "
                "Please set it to your Telegram API token."
            )

        return Client(token=os.environ['TELEGRAM_TOKEN'], debug=debug)

    def send(self, msg: str, chat_id: str, parse_mode: str = None) -> Dict[str, Any]:
        """Send a message to a chat."""

        params = {
            'chat_id': chat_id,
            'text': msg,
            'parse_mode': parse_mode,
        }

        if self.debug:
            print(f"params: {params}")
            print(f"Sending message to chat {chat_id}: {msg}")

        r = requests.get(
            f'https://api.telegram.org/{self.token}/sendMessage',
            params=params
        )

        if self.debug:
            print(r.text)

        r.raise_for_status()
        
        return r.json()
