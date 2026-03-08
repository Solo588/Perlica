'''
main - runs the overall workflow
'''

from watch_telegram import main as w_telegram
from SRouter import ROUTE_workflow as ROUTE

async def workflow():
    event = await event_queue.get()
    ROUTE(event)




def main():
    workflow()

if __name__ == "__main__":
    main()