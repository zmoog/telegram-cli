import os
from typing import Any, Dict

import requests


class Client:
    """Telegram client."""

    def __init__(self, token: str, verbose: bool = False):
        self.token = token
        self.verbose = verbose

    @staticmethod
    def from_environment(verbose: bool = False) -> "Client":
        """Create a client from the TELEGRAM_TOKEN environment variable."""

        if "TELEGRAM_TOKEN" not in os.environ:
            raise Exception(
                "TELEGRAM_TOKEN environment variable not found. "
                "Please set it to your Telegram API token."
            )

        return Client(token=os.environ['TELEGRAM_TOKEN'], verbose=verbose)

    def send(self, msg: str, chat_id: str, parse_mode: str = None) -> Dict[str, Any]:
        """Send a message to a chat."""

        params = {
            'chat_id': chat_id,
            'text': msg,
            'parse_mode': parse_mode,
        }

        if self.verbose:
            print(f"params: {params}")
            print(f"Sending message to chat {chat_id}: {msg}")

        r = requests.get(
            f'https://api.telegram.org/{self.token}/sendMessage',
            params=params
        )

        if self.verbose:
            print(r.text)

        r.raise_for_status()
        
        return r.json()


    # https://core.telegram.org/api/files
    def send_document(self, file_path: str, chat_id: str, caption: str = None) -> Dict[str, Any]:
        """Send a file to a chat."""

        params = {
            'chat_id': chat_id,
        }

        if caption:
            params['caption'] = caption

        if self.verbose:
            print(f"params: {params}")
            print(f"Sending file to chat {chat_id}: {file_path}")

        with open(file_path, 'rb') as f:
            r = requests.post(
                f'https://api.telegram.org/{self.token}/sendDocument',
                params=params,
                # files={'document': file_path}
                files={'document': f}
            )

        if self.verbose:
            print(r.text)

        r.raise_for_status()

        return r.json()
