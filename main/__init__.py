#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 13384432, cast=int)
API_HASH = config("API_HASH", ea9db4503ed7088b788e06dfd818e00e)
BOT_TOKEN = config("BOT_TOKEN", 7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", ANUBIS0X1)
AUTH = config("AUTH", 6169288210, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
