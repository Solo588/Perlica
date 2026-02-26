'''
Spam mentimeter poll
Input: 
    mentimeter code
    word
    spam times

Output:
    return spammed times
'''
# Pending add pausing and cancel

# from playwright import sync_playwright
# import time

import asyncio

async def run_spam(code, times, word):
    MENTI_CODE = code
    WORD = word
    TIMES = times
    for i in range(TIMES):
        print(WORD)
        await asyncio.sleep(0.5)
    return TIMES

'''
work in progress
'''