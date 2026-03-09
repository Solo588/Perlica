'''
main - runs the overall workflow
'''

from watch_telegram import event_queue
import asyncio

import state

from watch_telegram import watch_telegram as w_telegram
from SRouter import ROUTE_workflow as ROUTE

async def workflow():
    while state.online:
        print("\nnew loop\n")
        event = await event_queue.get()
        print("\nget queued event\n")
        await ROUTE(event)




async def main():
    asyncio.create_task(w_telegram())
    await workflow()

if __name__ == "__main__":
    asyncio.run(main())