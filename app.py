'''
APP - runs the overall workflow
'''

from watch_telegram import main as w_telegram

def workflow():
    w_Telegram = w_telegram()
    print(f"  -  {w_Telegram}")

def main():
    workflow()

if __name__ == "__main__":
    main()