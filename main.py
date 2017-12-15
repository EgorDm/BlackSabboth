import os
import time
from os.path import join, dirname

import telepot
from dotenv import load_dotenv
from telepot.delegate import include_callback_query_chat_id, pave_event_space, per_chat_id, create_open
from telepot.loop import MessageLoop

from bot import BlackSabboth


def on_callback_query(args):
    print(args)


def main():
    bot = telepot.DelegatorBot(os.environ.get("TELEGRAM_KEY"), [
        include_callback_query_chat_id(
            pave_event_space())(
            per_chat_id(), create_open, BlackSabboth, timeout=10),
    ])

    MessageLoop(bot).run_as_thread()
    print('Listening ...')

    while 1: time.sleep(10)


if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    main()
