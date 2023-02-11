import click

from . import telegram


@click.group()
@click.version_option()
def cli():
    "Python CLI tool and library for sending messages to Telegram"


@cli.group()
# @click.option(
#     '--project-id',
#     '-p',
#     type=click.INT,
#     multiple=True)
@click.pass_context
def message(ctx: click.Context):
    ctx.ensure_object(dict)
    # ctx.obj['project_id'] = project_id


@message.command(name="send")
# @click.option(
#     "--start-date",
#     type=click.DateTime(),
#     default=as_str(now - dt.timedelta(hours=24)),
#     help="Start date (default: 24 hours ago)"
# )
@click.option(
    "--text",
    # type=click.DateTime(),
    required=True,
)
@click.option(
    "--chat-id",
    # type=click.DateTime(),
    required=True,
)
@click.pass_context
def send(ctx: click.Context, text: str, chat_id: str):
    
    client = telegram.Client.from_envorinment()
    resp = client.send(text, chat_id)

    message_id = resp.get("result", {}).get("message_id", "No message id found")
    click.echo(f"message-id: {message_id}")
