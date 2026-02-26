

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

stop_event = asyncio.Event()

# ---- TASK 1: print sigma every 0.4s ----
async def sigma_task():
    i=0
    while not stop_event.is_set():
        print(f"sigma{i}")
        i+=1
        await asyncio.sleep(1)

# ---- TASK 2: send omega every 1s ----
async def omega_task(app):
    # we store last chat id dynamically
    while not stop_event.is_set():
        if app.bot_data.get("chat_id"):
            await app.bot.send_message(
                chat_id=app.bot_data["chat_id"],
                text="omega"
            )
        await asyncio.sleep(1)

# ---- TELEGRAM MESSAGE HANDLER ----
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # store chat id once someone messages bot
    context.application.bot_data["chat_id"] = update.effective_chat.id

    if text == "stop":
        await update.message.reply_text("Stopping...")
        stop_event.set()

# ---- MAIN ----
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # start background tasks
    asyncio.create_task(sigma_task())
    asyncio.create_task(omega_task(app))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # wait until stop_event triggered
    await stop_event.wait()

    await app.stop()
    await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())