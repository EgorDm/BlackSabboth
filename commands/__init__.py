from commands.base_command import BaseCommand
from commands.standard_commands import GreetCommand
from commands.test_commands import TestCommand
from commands.music_info_commands import ArtistCommand, AlbumCommand, TrackCommand

routes = {
    'greet': GreetCommand,
    'test': TestCommand,
    'artist': ArtistCommand,
    'album': AlbumCommand,
    'track': TrackCommand,
}