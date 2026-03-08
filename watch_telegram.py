"""
watch_telegram.py

Job:
- start telegram listener
- wait for next incoming text message
- return it as an event
"""

from dotenv import load_dotenv
import os
import asyncio

from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

import actions.send_telegram as sTele

import state

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PLATFORM = "telegram"


async def watch_telegram():
    """
    Waits for one telegram message and returns it as an event.
    Stops cleanly if state.online becomes False.
    """
    event_queue = asyncio.Queue()

    async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not state.online:
            return

        message = update.effective_message
        user = update.effective_user

        if message is None or user is None:
            return

        if not message.text:
            return

        event = {
            "platform": PLATFORM,
            "user_id": user.id,
            "chat_id": message.chat_id,
            "text": message.text
        }

        await event_queue.put(event)

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(~filters.COMMAND, on_message))

    try:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()

        sTele(on_message.user.id,"Telegram listening...")

        while state.online:
            try:
                event = await asyncio.wait_for(event_queue.get(), timeout=0.5)
                return event
            except asyncio.TimeoutError:
                continue

        return None

    finally:
        sTele(on_message.user.id,"Stopping telegram polling...")
        if app.updater and app.updater.running:
            await app.updater.stop()
        await app.stop()
        await app.shutdown()