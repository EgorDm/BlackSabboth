messages = {
    '404_called': 'Could not find {} called {}!',
    '404': 'Resource could not be found!',

    # Views
    'artist': '*{}*\n*Followers:* {}\n*Genres:* {}',
    'album': '*{}* ({})\nBy _{}_\n*Genres:* {}\n*Tracks:* {}',
    'track': '*{}*\nBy _{}_\n*Duration:* {:.2f} min',

    # Actions
    'view_albums': 'View albums',
    'view_tracks': 'View tracks',
    'next_page': 'Next page',
    'previous_page': 'Previous page',
    'list_items': '*Page {} of {}*\nFollowing items are found:',
    'open_spotify': 'Open in Spotify',
}


def msg(name, *args):
    return messages[name].format(*args)
