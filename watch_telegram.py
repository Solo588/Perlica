'''
Watch telegram

Next up:
    1. Move out menti spam
    2. process stickers and gifs (and move them out maybe)

    
purpose:
    - toggle quick queries 
        1. Public
        2. commands
        3. health
        4. kill
        5. status

    - filter
        1. Sticker
        2. text > 10 word


inputs: 
    telegram: text, stickers and gifs

outputs: 
                event = {
                    "platform": platform,
                    "user_id": user_id,
                    "text": text
                }

Ignores: command, over 10 words

Special commands:
- "commands"    -> view commands
- "health"      -> returns bot status
- "kill"        -> shuts bot down
'''
#---------------------------------------------------------------------------------
#.env shyt
from dotenv import load_dotenv
import os
load_dotenv()

#temporary: health and runtime shyt (will move to seperate later)
import time 
import psutil
from actions.spam_mentimeter import run_spam

#keep
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from telegram.error import TelegramError, NetworkError, TimedOut


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
platform = "telegram"
user_id = ""

public = False

START_TIME = time.time() #temporary

# ---------- helpers (temporary) -------------
def get_health():
    uptime = int(time.time() - START_TIME)
    proc = psutil.Process(os.getpid())

    ram_mb = proc.memory_info().rss / 1024 / 1024
    cpu_pct = proc.cpu_percent(interval=0.2)

    return (
        f"perlica health\n"
        f"- uptime: {uptime}s\n"
        f"- ram: {ram_mb:.1f} MB\n"
        f"- cpu: {cpu_pct:.1f}%\n"
        f"- pid: {os.getpid()}\n"
    )


# ------------ telegram handler --------------
async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("watch_telegram") #for debugging
    user = update.message.from_user
    message = update.message
    text = message.text
    user_id = message.from_user.id

    global public

    event = {
        "platform": platform,
        "user_id": user_id,
        "text": text
    }

    #print(user_id," || ", ADMIN_ID, " || Public: ", public, " || Same_ID: ", user_id==ADMIN_ID)
    # ------ filters ------
    ''' For future use cases'''
    if not message.text:
        await update.message.reply_text("cannot take anything other than text rn")
        text = ""
        print (event)
        return 
    
    word_count = len(text.split())

    if word_count>10:
        await update.message.reply_text("aight bro shit's too long")
        text = "length limit"
        return

    # ------------------ ADMIN CONTROL -------------------
    if user_id != ADMIN_ID and not public:
        await message.reply_text("currently not available to public")
        print(event)
        return
    
    if user_id == ADMIN_ID and message.text:
        if text.lower() == "commands":
            await message.reply_text(
                "status - check public status\n"
                "make public/private - toggle option\n" 
                "health - computer health\n"
                "kill - turn off\n"
                "menti spam (code), (times)")
            print(event)
            return

        elif text.lower() == "status":
            await message.reply_text(f"Public: {public}")
            print(event)
            return
        
        elif text.lower() == "make public":
            if public:
                await message.reply_text("Perlica is already public")
            else: 
                public = True
                await message.reply_text("Perlica made public")
            return
        
        elif text.lower() == "make private":
            if not public:
                await message.reply_text("Perlica is already private")
            else:  
                public = False
                await message.reply_text("Perlica made private")
            return

        elif text.lower() == "kill":
            await message.reply_text("perlica shutting down.")
            await context.application.stop()
            print (event)
            print ("Perlica shutted down.")
            return
        
        # LLM's job
        elif text.lower().startswith("menti spam"):
            parse = text.split(' ')

            if len(parse) != 5:
                await message.reply_text("INVALID FORMAT")
                return
            
            code = parse[2]
            times = parse[3]
            word = parse [4]

            if len(code) != 6 or not code.isdigit():
                await message.reply_text("code is incorrect")
                return
            
            try:
                times = int(times)
            except ValueError:
                await message.reply_text("times must be a number")
                return
            
            if times > 10:
                await message.reply_text("too many times")
                return
            
            run_spam(code, times, word)

            return

    #Temporary: Health and kill
    # ---- control commands ----
    if text.lower() == "health":
        await message.reply_text(get_health())
        await message.reply_text(
            f"How to read:\n"
            f"- uptime: js for fun\n"
            f"- ram: 50~250MB, rising = ~memory leak\n"
            f"- CPU: ~<10% normal\n"
            f"- PID: session number")
        print (event)
        return
    
    '''output'''
    await update.message.reply_text(text) #testing
    print (event)

#script
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(~filters.COMMAND, on_message))
    print("Telegram listening ...")
    app.run_polling()

#for powershell
if __name__ == "__main__":
    main()
