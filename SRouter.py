'''
    router from watch_telegram to hardcoded or LLM
'''

from dotenv import load_dotenv
import os
load_dotenv()

import state
from LLM import LLM

from actions.fastCMD import cmd as Fcmd

ADMIN_ID = int(os.getenv("ADMIN_ID"))
Admin = False
WhiteListStatus = ""
cmd_list = state.cmdList
WLList = state.wlList

# This will have to be editable through perlica_console or by bot later.
WhiteListUsers = [ADMIN_ID]

def check_identity(id):
    global WhiteListStatus
    global Admin

    if id == ADMIN_ID:
        return "Admin"
    
    elif id in WLList:
        return "whiteList"
    
    return None
        

def Rcmd(text,cid):
    Fcmd(text,cid)
    return

def ROUTE_workflow(event,context):
    wl_status = check_identity(event["user_id"])
    textLowerSplit = event["text"].lower().split()
    result = any(word in cmd_list for word in textLowerSplit)

    cid = event["chat_id"]

    if wl_status == "Admin":
        Rcmd(event["text"], cid)

    elif wl_status == "whiteList":
        LLM_ROUTE(LLM(event["text"], wl_status, cid))
    return

def LLM_ROUTE(output):
    print(f"\n\noutput\n\n")