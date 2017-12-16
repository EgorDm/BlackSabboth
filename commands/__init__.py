from commands.base_command import BaseCommand, Message
from commands.standard_commands import GreetCommand
from commands.test_commands import TestCommand
from commands.music_info_commands import ArtistCommand, AlbumCommand, TrackCommand
from commands.lyric_game_commands import StartGameCommand, StopGameCommand, GuessGameCommand, NextLineCommand, StatsGameCommand

routes = {
    'greet': GreetCommand,
    'test': TestCommand,
    'artist': ArtistCommand,
    'album': AlbumCommand,
    'track': TrackCommand,
    'game': StartGameCommand,
    'stop': StopGameCommand,
    'skip': NextLineCommand,
    'guess': GuessGameCommand,
    'stats': StatsGameCommand,
}