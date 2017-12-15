from os.path import join, dirname

from dotenv import load_dotenv

import logic


def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    print('Starting tests')
    cs = logic.SpotifyController()

    print(cs.find_artist('dio', id='4CYeVo5iZbtYGBN4Isc3n6'))


if __name__ == '__main__': main()