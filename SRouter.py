'''
    router from watch_telegram to hardcoded or LLM
'''

from dotenv import load_dotenv
import os
load_dotenv()

import state
import LLM

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
        WhiteListStatus = "Admin"
        Admin = True
        return WhiteListStatus
    
    elif id in WLList:
        WhiteListStatus = "whiteList"
        return WhiteListStatus
        

def Rcmd(text):
    Fcmd(text)

def ROUTE_workflow(event):
    check_identity(event["user_id"])
    textLowerSplit = event["text"].lower().split()
    result = any(word in cmd_list for word in textLowerSplit)

    if Admin and result:
        Rcmd(event["text"])

    else:
        LLM.LLM(event["text"], )

def LLM_ROUTE():
    '''
    LLM output:
        - 
    '''