from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
SESSION = os.environ.get("TERMUX")
sedthon = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
sedthon.start()