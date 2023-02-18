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
            ["message", "send", "--text", "'Hello, world!'", "--chat-id", "123456"],
            env=env,
        )
        assert result.exit_code == 0
        assert "message-id: 719" in result.output


@pytest.mark.vcr
@pytest.mark.block_network
def test_send_markdown():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["message", "send", "--parse-mode", "MarkdownV2", "--text", "welcome to this **fucking** world", "--chat-id", "123456"],
            env=env,
        )
        assert result.exit_code == 0
        assert "message-id: 720" in result.output


@pytest.mark.vcr
@pytest.mark.block_network
def test_send_html():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["message", "send", "--parse-mode", "HTML", "--text", "welcome to this <b>fucking</b> world", "--chat-id", "123456"],
            env=env,
        )
        assert result.exit_code == 0
        assert "message-id: 721" in result.output
