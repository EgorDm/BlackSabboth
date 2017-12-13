import time
from os.path import join, dirname

from dotenv import load_dotenv
from telepot.loop import MessageLoop

from bot import BlackSabboth


def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    bot = BlackSabboth()
    MessageLoop(bot).run_as_thread()
    print('Listening ...')
    while 1: time.sleep(10)


if __name__ == "__main__": main()
