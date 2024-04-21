import tempfile

import pytest

from click.testing import CliRunner
from telegram_cli.cli import cli


env = {
    "TELEGRAM_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_send_document_with_caption(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem():
        with tempfile.NamedTemporaryFile(mode='w') as temp_file:
            temp_file.write("This is a test file.")
            temp_file.flush()
            temp_file = temp_file.name

            result = runner.invoke(
                cli,
                ["message", "send-document", "--file", temp_file, "--chat-id", "123456", "--caption", "This is my favourite license"],
                env=env,
            )
            assert result.exit_code == 0
            assert "message-id: 2131" in result.output
