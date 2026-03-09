'''
main - runs the overall workflow
'''

from watch_telegram import event_queue
import asyncio

from watch_telegram import main as w_telegram
from SRouter import ROUTE_workflow as ROUTE

async def workflow():
    while True:
        event = await event_queue.get()
        ROUTE(event)




def main():
    asyncio.run(workflow())

if __name__ == "__main__":
    main()