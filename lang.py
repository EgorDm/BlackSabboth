messages = {
    '404_called': 'Could not find {} called {}!',
    '404': 'Resource could not be found!',
    '404_tracks': 'Could not find tracks for: {}!',
    'no_source': 'Please specity a source type. Available [artist, album, track]',
    'source_empty': 'Source unfortunately has no lyrics available.',

    # Views
    'artist': '*{}*\n*Followers:* {}\n*Genres:* {}',
    'album': '*{}* ({})\nBy _{}_\n*Genres:* {}\n*Tracks:* {}',
    'track': '*{}*\nBy _{}_\n*Duration:* {:.2f} min',
    'game_already_started': 'You are currently in a game! Stop it with /stop',
    'game_started': 'Game has started! Goodluck!',
    'game_not_exists': 'There has never been a game!',
    'game_stopped': 'Game has now stopped!',
    'game_guess_right': '*{}* got it *right* and *recieved {}* points!\nThe line was:\n_{}_',
    'game_guess_wrong': '*{}* got it *wrong*!\nYou picked:\n_{}_\nThe line was:\n_{}_',
    'game_quess': '*Try guessing next line:*\n_{}_\n...',
    'game_stat': '*{}* has *{}* points',

    # Actions
    'view_albums': 'View albums',
    'view_tracks': 'View tracks',
    'next_page': 'Next page',
    'previous_page': 'Previous page',
    'list_items': '*Page {} of {}*\nFollowing items are found:',
    'open_spotify': 'Open in Spotify',
    'start_game_with': 'Lyrics quiz',
}


def msg(name, *args):
    return messages[name].format(*args)
