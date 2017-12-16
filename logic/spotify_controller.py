import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyController:
    def __init__(self, bot):
        self.bot = bot
        ccm = SpotifyClientCredentials(os.environ.get('SPOTIFY_CLIENT'), os.environ.get('SPOTIFY_SECRET'))
        self.sapi = spotipy.Spotify(client_credentials_manager=ccm)

    def find_artist(self, q, id=None):
        try:
            if id is None: return self.sapi.search(q='artist:' + q, type='artist')['artists']['items'][0]
            return self.sapi.artist(id)
        except: pass
        return None

    def artist_albums(self, id, limit=5, offset=0):
        try:
            res = self.sapi.artist_albums(id, limit=limit, offset=offset, album_type='album,single')
            return res['total'], res['items']
        except: pass
        return None

    def artist_top_tracks(self, id):
        try:
            return self.sapi.artist_top_tracks(id)['tracks']
        except: pass
        return None

    def find_album(self, q=None, id=None):
        try:
            if id is None:
                id = self.sapi.search(q='album:' + q, type='album')['albums']['items'][0]['id']
            return self.sapi.album(id)
        except: pass
        return None

    def find_track(self, q=None, id=None):
        try:
            if id is None:
                id = self.sapi.search(q='track:' + q, type='track')['tracks']['items'][0]['id']
            return self.sapi.track(id)
        except: pass
        return None

    def album_tracks(self, id, limit=6, offset=0):
        try:
            res = self.sapi.album_tracks(id, limit=limit, offset=offset)
            return res['total'], res['items']
        except: pass
        return None

    def pick_photo(self, images, desired_size=512):
        if len(images) == 0: return None
        images = sorted(images, key=lambda image: abs(image['width'] - desired_size))
        return images[0]['url']
