import pytest

from click.testing import CliRunner
from telegram_cli.cli import cli


env = {
    "TELEGRAM_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_send():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["message", "send", "--text", "'Hello, world!'", "--chat-id", "161035319"],
            env=env,
        )
        assert result.exit_code == 0
        assert "message-id: 665" in result.output
