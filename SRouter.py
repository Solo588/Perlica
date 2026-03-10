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
    
    return
        

async def Rcmd(text,cid):
    await Fcmd(text,cid)
    return

async def ROUTE_workflow(event):
    wl_status = check_identity(event["user_id"])
    textLowerSplit = event["text"].lower().split()
    result = textLowerSplit[0] in cmd_list

    cid = event["chat_id"]

    if wl_status == "Admin" and result:
        print("requested cmd")
        await Rcmd(event["text"], cid)

    elif wl_status == "whiteList" or wl_status == "Admin":
        print("routed to LLM")
        LLM_ROUTE(await LLM(event["text"], wl_status, cid))
    return

def LLM_ROUTE(output):
    print(f"\n\n{output}\n\n")