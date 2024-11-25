# Simple Mastodon Bot Template

To run a Mastodon bot, first you need to create a Mastodon account that will
represent the bot. Before creating the account, check your instance's rules to
make sure it allow publishing automated content.

### Use this code only to make good, useful things, and be nice to people.

## Initialization

1. In Mastodon go to your Account Preferences -> Development -> New Application
2. Create a new application and copy the values 
3. Copy `.env-example` to `.env` and fill in the variables with values from previous point
4. Create a new Python virtual env `python3 -m venv venv`
5. Install dependencies with `pip install -r requirements.txt`

## Creating the bot

Edit the `prepare_toot_body` method in `services.py` to set what the bot should
be sending. All toot generation logic should be placed in that service.

## Running the bot

Run the bot with `python main.py`. Running `python main.py --dry-run` will only
print the toot body, not send it to Mastodon

## Deployment
Copy the code to the server that will be hosting the bot. Use `scp` or make a
fork of this repo and publish it to a git server. Once the files are copied, SSH
to the server and create the venv and install the dependencies as in the
Initialization step. Make sure that the `.env` is present on the server as well.
The simplest way to run the bot periodically is to set a cron job. To edit cron,
run `crontab -e`. Then in the opened file add a expression to run the bot, for
example:
```sh
0 * * * * /home/pi/scripts/mastodon-bot/venv/bin/python /home/pi/scripts/mastodon-bot/main.py
```
First part is the cron expressions, this one means "run every hour", next is the
absolute path to the Python binary in the venv you created, and finally the
absolute path to the `main.py` file that runs the bot.