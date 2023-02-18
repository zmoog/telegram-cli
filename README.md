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

### Basic

For sending a simple text message to a user o group, run:

    export TELEGRAM_TOKEN='bot123456:de4dbeefde4dbeefde4dbeefde4dbeefde4dbeef' 

    $ tgm message send --text 'Hello' --chat-id 123456
    message-id: 676

### Text from a stream (file or stdin)

For sending the content of a text file as message text:

    # you have a text file with a message you want to send
    echo "hey dude" > message.txt 

    # (1) use the `--text-file` option
    tgm message send --chat-id 123456 --text-file message.txt 

    # (2) use `<`
    tgm message send --chat-id 123456 < message.txt 

    # (3) use `|`
    cat message.txt | tgm message send --chat-id 123456
    # or
    echo "hey dude, it's me again" | tgm message send --chat-id 123456 

    # (4) type your message and send it by typing `CTRL+D`
    tgm message send --chat-id 123456
    Hey dude, yeah it's me again!
    <CTRL+D>

### Parse modes

For using one of the supported parse modes (`MarkdownV2` or `HTML`) of the entities in the message, run:

    tgm message send --parse-mode "MarkdownV2" --text '**Hello**' --chat-id 123456
    
    tgm message send --parse-mode "HTML" --text '<b>Hello</b>' --chat-id 123456

See the available [formatting options](https://core.telegram.org/bots/api#formatting-options) to learn how to use `--parse-mode`.

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
