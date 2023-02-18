import io

import pytest

from click.testing import CliRunner
from telegram_cli.cli import cli


env = {
    "TELEGRAM_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_send_from_a_file():
    runner = CliRunner()
    with runner.isolated_filesystem():

        # pick a message to send
        message_text = "Hello, world!"

        # Create a file with some text
        with open("message.txt", "w") as f:
            f.write("Hello, world!")
        
        # Send the message
        result = runner.invoke(
            cli,
            ["-v", "message", "send", "--chat-id", "123456", "--text-file", "message.txt"],
            env=env,
        )

        # Check the result
        assert result.exit_code == 0
        assert message_text in result.output


@pytest.mark.vcr
@pytest.mark.block_network
def test_send_reading_to_stdin():
    runner = CliRunner()
    with runner.isolated_filesystem():

        # pick a message to send
        message_text = "Hello, world!"

        # Send the message
        result = runner.invoke(
            cli,
            ["-v", "message", "send", "--chat-id", "123456"],
            env=env,
            input=message_text,
        )

        # Check the result
        assert not result.exception
        assert result.exit_code == 0
        assert message_text in result.output
