import re

from telethon.sync import TelegramClient

# Name of the session file
name = "tg"

# Get from https://my.telegram.org/
api_id =
api_hash =

# Channel Username
channel_username =

# Conditions of deleting messages
max_id =
regex_string =

with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(channel_username):
        if message.id < max_id and re.search(regex_string, message.message):
            message.delete()
