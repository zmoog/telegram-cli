import sys
from typing import TextIO

import click

from . import telegram


@click.group()
@click.version_option()
@click.option('--verbose', '-v', is_flag=True, help="Enable verbose mode")
@click.pass_context
def cli(ctx: click.Context, verbose: bool):
    "Python CLI tool and library for sending messages to Telegram"
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose

@cli.group()
@click.pass_context
def message(ctx: click.Context):
    ctx.ensure_object(dict)


@message.command(name="send")
@click.option(
    "--text",
    help="Text to send. If not provided, text will be read from a file or stdin.",
    default=None,
)
@click.option(
    "--text-file", 
    help="Text file to read from. If not provided, stdin will be used.",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=True),
    default="-",
)
@click.option(
    "--chat-id",
    required=True,
)
@click.option(
    '--parse-mode',
    type=click.Choice(
        ['HTML', 'MarkdownV2'],
        case_sensitive=False
    ),
    default=None,
)
@click.pass_context
def send(ctx: click.Context, text: str, text_file: TextIO, chat_id: str, parse_mode: str):
    """Send a text message to a chat."""
    
    client = telegram.Client.from_environment(verbose=ctx.obj["verbose"])

    if text:
        message_text = text
    elif text_file in ("-", "stdin"):
        message_text = sys.stdin.read()
    else:
        with open(text_file, "r") as f:
            message_text = f.read()

    resp = client.send(message_text, chat_id, parse_mode=parse_mode)

    message_id = resp.get("result", {}).get("message_id", "No message id found")
    click.echo(f"message-id: {message_id}")
