import click
from dotenv import load_dotenv

from services import BotService, ConfigService, MastodonService


@click.command()
@click.option("--dry-run", is_flag=True)
def main(dry_run):
    load_dotenv()

    if not ConfigService().validate_config():
        print("One or more env variables are missing, check your .env file!")
        exit()

    bot_service = BotService()
    body = bot_service.prepare_toot_body()

    if dry_run:
        print(body)
    else:
        bot_service = MastodonService()
        bot_service.post(body)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
