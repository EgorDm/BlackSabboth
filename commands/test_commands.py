import os
import spotipy
import commands
from spotipy.oauth2 import SpotifyClientCredentials


class TestCommand(commands.BaseCommand):
    def __init__(self, handler, command, args):
        super().__init__(handler, command, args)
        client_credentials_manager = SpotifyClientCredentials(client_id=os.environ.get('SPOTIFY_CLIENT'),
                                                              client_secret=os.environ.get('SPOTIFY_SECRET'))
        self.sapi = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def execute(self):
        super().execute()
        print(self.sapi.search(q='artist:' + ' '.join(self.args), type='artist'))
        self.msg('yeaa')
