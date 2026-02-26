'''
Action_Access - assign avaliable actions to diff status
input:
    user_id

output: 
    available_actions.txt
    run immidiate tasks
'''

#.env shyt
from dotenv import load_dotenv
import os
load_dotenv()

ADMIN_ID = int(os.getenv("ADMIN_ID"))
ACTION_FILE = "available_actions.txt"

actions = ['spam mentimeter', 'send telegram', 'whitelist']

def check(user_id, file=ACTION_FILE):
    if user_id == ADMIN_ID:
        

