'''
    codes that runs the fast response CMD

    Can be accessed by bot by writing the text. but usually these are for human prompters.
'''

import time 
import psutil
import state

from send_telegram import Message as Msend
from send_telegram import console as console
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import watch_telegram as w_telegram

send = ""
public = state.public

id = "import" #imported

async def cmd(text, context=None): 
    global id #need imports !!! 
    global send
    global public

    if text.lower() == "commands":
        send = (
            "status - check public status\n"
            "make public/private - toggle option\n" 
            "health - computer health\n"
            "kill - turn off\n"
            "menti spam (code), (times)" 
        )
        return Msend(id, send)
    
    elif text.lower() == "status":
        send = f"Public: {public}"
        return Msend(id, send)

    elif text.lower() == "make public":
        if public:
            send = "Perlica is already public"
        else: 
            state.public = True
            send = "Perlica made public"
        return Msend(id, send)

    elif text.lower() == "make private":
        if not public:
            send = "Perlica is already private"
        else:  
            state.public = False
            send = "Perlica made private"
        return Msend(id, send)

    elif text.lower() == "kill":
        send = ("perlica shutting down.")
        state.online = False
        await context.application.stop()
        Csend = "Perlica shutted down."
        print ("Perlica shutted down.")
        return Msend(id, send), console(id, Csend)
