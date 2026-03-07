''' 
Send Telegram
'''

#.env shyt
from dotenv import load_dotenv
import os
load_dotenv()

#keep
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from telegram.error import TelegramError, NetworkError, TimedOut
from telegram import Bot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CONSOLE_TOKEN = os.getenv("SECONDARY_BOT_TOKEN")

main_bot = Bot(token=BOT_TOKEN)
console_bot = Bot(token=CONSOLE_TOKEN)

async def console(id, text):
    await console_bot.send_message(
        chat_id=id,
        text=text
    )

async def Message(id, text):
    await main_bot.send_message(
        chat_id=id,
        text=text
    )