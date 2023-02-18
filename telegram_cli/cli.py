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
    required=True,
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
    default=None
)
@click.pass_context
def send(ctx: click.Context, text: str, chat_id: str, parse_mode: str):
    
    client = telegram.Client.from_envorinment(verbose=ctx.obj["verbose"])
    resp = client.send(text, chat_id, parse_mode=parse_mode)

    message_id = resp.get("result", {}).get("message_id", "No message id found")
    click.echo(f"message-id: {message_id}")
