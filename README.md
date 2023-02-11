# telegram-cli

[![PyPI](https://img.shields.io/pypi/v/telegram-cli.svg)](https://pypi.org/project/telegram-cli/)
[![Changelog](https://img.shields.io/github/v/release/zmoog/telegram-cli?include_prereleases&label=changelog)](https://github.com/zmoog/telegram-cli/releases)
[![Tests](https://github.com/zmoog/telegram-cli/workflows/Test/badge.svg)](https://github.com/zmoog/telegram-cli/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/zmoog/telegram-cli/blob/master/LICENSE)

Python CLI tool and library for sending messages to Telegram

## Installation

Install this tool using `pip`:

    pip install telegram-cli

## Usage

For sending a simple text message to a user o group, run:

    export TELEGRAM_TOKEN='bot123456:de4dbeefde4dbeefde4dbeefde4dbeefde4dbeef' 

    $ tgm message send --chat-id 123456 --text 'Hello'
    message-id: 676

For help, run:

    telegram-cli --help

You can also use:

    python -m telegram_cli --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd telegram-cli
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
