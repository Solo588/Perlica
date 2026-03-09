'''
    health.py
    checking health...
'''

import time 
import psutil
import os
import send_telegram
import asyncio

START_TIME = time.time()

async def get_health(cid):
    uptime = int(time.time() - START_TIME)
    proc = psutil.Process(os.getpid())

    ram_mb = proc.memory_info().rss / 1024 / 1024
    cpu_pct = proc.cpu_percent(interval=0.2)

    send = (
        f"perlica health\n"
        f"- uptime: {uptime}s\n"
        f"- ram: {ram_mb:.1f} MB\n"
        f"- cpu: {cpu_pct:.1f}%\n"
        f"- pid: {os.getpid()}\n"
    )

    await send_telegram.Message(cid, send)

    return 