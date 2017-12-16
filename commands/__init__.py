from commands.base_command import BaseCommand, Message
from commands.standard_commands import HelpCommand
from commands.music_info_commands import ArtistCommand, AlbumCommand, TrackCommand
from commands.lyric_game_commands import StartGameCommand, StopGameCommand, GuessGameCommand, NextLineCommand, StatsGameCommand

routes = {
    'help': HelpCommand,
    'start': HelpCommand,
    'artist': ArtistCommand,
    'album': AlbumCommand,
    'track': TrackCommand,
    'game': StartGameCommand,
    'stop': StopGameCommand,
    'skip': NextLineCommand,
    'guess': GuessGameCommand,
    'stats': StatsGameCommand,
}