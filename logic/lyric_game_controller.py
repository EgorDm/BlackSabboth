import random
import sqlite3
import time

from PyLyrics import PyLyrics

import lang
#import logic

SONG_CHANGE_PROB = 0.1
N_PREVIOUS_LINES = 3
N_CHOICES = 4

lyric_cache = {}


def _process_lyrics(lyrics):
    lyrics = list(filter(None, lyrics))
    ret = []
    dup_count = 0
    for i in range(len(lyrics)):
        line = lyrics[i]
        if i + 1 < len(lyrics) and line.lower() == lyrics[i+1]:
            dup_count += 1
            continue
        if dup_count > 0: line += ' _[x{}]_'.format(dup_count)
        ret.append(line)
        dup_count = 0

    return lyrics


def get_lyrics(name):
    artist, title = name.split(' - ', 1)
    if name in lyric_cache: return lyric_cache[name]
    try:
        lyrics = PyLyrics.getLyrics(artist, title)
        lyric_cache[name] = _process_lyrics(lyrics.splitlines())
        return lyrics
    except ...: return None


class GameException(Exception):
    pass


class GameSession:
    def __init__(self, chat_id, song_names):
        self.chat_id = chat_id
        self.song_names = song_names
        self.started_date = time.time()
        self.scores = {}
        self.current_song = self.song_names[0]
        self.cursor = 0
        self.randomize_song()
        self.randomize_line()

    def randomize_song(self):
        if len(self.song_names) == 0:
            self.current_song = None
            return
        self.current_song = random.choice(self.song_names)
        if len(self.lyrics) == 0:
            self.song_names.pop(self.current_song)
            self.randomize_song()

    def randomize_line(self):
        if random.randint(0, 100) > 100 * SONG_CHANGE_PROB: self.randomize_song()
        if self.current_song is None:
            self.cursor = -1
            return

        self.cursor = random.randint(N_PREVIOUS_LINES + 1, len(self.lyrics) - N_PREVIOUS_LINES - 1)

    def get_guess_lines(self):
        return self.lyrics[self.cursor - N_PREVIOUS_LINES:self.cursor]

    def get_current_line(self):
        return self.lyrics[self.cursor]

    def get_choices(self):
        line = self.get_current_line()
        lyrics = self.lyrics
        ret = [line]
        while len(ret) < N_CHOICES:
            cand = lyrics[random.randint(0, len(self.lyrics) - 1)]
            if cand not in ret: ret.append(cand)
        random.shuffle(ret)
        return ret

    def add_score(self, player_id, score):
        if player_id not in self.scores: self.scores[player_id] = 0
        self.scores[player_id] += score

    def add_guess(self, player_id, guess):
        current_line = self.get_current_line()
        # accuracy = logic.is_ci_lemma_stopword_set_match(current_line, guess)
        # score = accuracy * len(current_line.split())
        score = 5 if guess == current_line else 0
        self.add_score(player_id, score)
        return score # accuracy,

    @property
    def lyrics(self): return get_lyrics(self.current_song)


class LyricGameController:
    sessions = {}

    def __init__(self, bot):
        """
        :param bot:
        :type bot: BlackSabbot
        """
        self.bot = bot
        self.conn = sqlite3.connect('data.db')

    def start_game(self, chat_id, source_type, name, id=None):
        if chat_id in self.sessions: raise GameException(lang.msg('game_already_started'))
        song_names = self._get_song_names(source_type, name, id)
        if len(song_names) == 0: raise GameException(lang.msg('404_tracks', name))
        self.sessions[chat_id] = GameSession(chat_id, song_names)
        # TODO: pick a song

    def stop_game(self, chat_id):
        if chat_id not in self.sessions: return False
        self.sessions.pop(chat_id)
        return True

    def _get_song_names(self, source_type, name, id=None):
        song_names = []
        songs = []
        if source_type == 'artist':
            if id is None:
                artist = self.bot.spotify_controller.find_artist(name)
                if artist is None: return []
                id = artist['id']
            songs = self.bot.spotify_controller.artist_top_tracks(id)
        if source_type == 'album':
            if id is None:
                album = self.bot.spotify_controller.find_album(name)
                if album is None: return []
                id = album['id']
            songs = self.bot.spotify_controller.album_tracks(id, 50)[1]
        if source_type == 'track':
            song = self.bot.spotify_controller.find_track(name, id)
            if song is None: return []
            songs = [song]

        if songs is None: return []
        for song in songs: song_names.append(f'{song["artists"][0]["name"]} - {song["name"]}')
        return song_names
