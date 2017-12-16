import os
import time
from os.path import join, dirname

from dotenv import load_dotenv
from telepot.loop import MessageLoop

from bot import BlackSabboth


def main():
    bot = BlackSabboth(os.environ.get("TELEGRAM_KEY"))
    # bot.setWebhook()
    MessageLoop(bot).run_as_thread()
    print('Listening ...')

    while 1: time.sleep(10)


if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    main()
