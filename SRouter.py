'''
    router from watch_telegram to hardcoded or LLM
'''

from dotenv import load_dotenv
import os
load_dotenv()

from actions.fastCMD import cmd as Fcmd

ADMIN_ID = int(os.getenv("ADMIN_ID"))
Admin = False
WhiteListStatus = ""
cmd_list = ["commands", "status", "public", "private", "kill", "menti", "spam"]
WLList = ["Admin", "whiteList", "unknown", "blackList"]

# This will have to be editable through perlica_console or by bot later.
WhiteListUsers = [ADMIN_ID]


def route(cmd, param1, param2):
    print()

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
    id = event["user_id"]
    textLowerSplit = event["text"].lower().split()
    result = any(word in cmd_list for word in textLowerSplit)
    if Admin:
        Rcmd(event["text"])