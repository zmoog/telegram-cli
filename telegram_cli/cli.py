import click

from . import telegram


@click.group()
@click.version_option()
def cli():
    "Python CLI tool and library for sending messages to Telegram"


@cli.group()
@click.pass_context
def message(ctx: click.Context):
    ctx.ensure_object(dict)


@message.command(name="send")
@click.option(
    "--text",
    required=True,
)
@click.option(
    "--chat-id",
    required=True,
)
@click.pass_context
def send(ctx: click.Context, text: str, chat_id: str):
    
    client = telegram.Client.from_envorinment()
    resp = client.send(text, chat_id)

    message_id = resp.get("result", {}).get("message_id", "No message id found")
    click.echo(f"message-id: {message_id}")
