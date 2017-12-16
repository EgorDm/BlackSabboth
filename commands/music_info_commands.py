import commands
import lang
import utils
from commands.presenters import ArtistPresenter, AlbumPresenter, AlbumsPresenter, TrackPresenter, ITEMS_PER_PAGE, TracksPresenter


class SpotifyCommand(commands.BaseCommand):
    def __init__(self, handler, message):
        super().__init__(handler, message)
        self.spotify = handler.bot.spotify_controller

    def execute(self):
        parent = self.get_var('p')
        if parent is not None: self.parent_action(parent)
        else: self.action()

    def action(self):
        pass

    def parent_action(self, id): pass

    def render_resource(self, resource, presenter, error_msg):
        if resource is None: return self.msg(error_msg)
        presenter().present(resource, self, self.sender())

    def _get_id(self): return self.get_var()

    def _keyboard_buttons(self, data): return [{"text": lang.msg('open_spotify'), "url": data['external_urls']['spotify']}]

    def _is_edit(self): return int(self.get_var('rep', 0)) == 1


class ArtistCommand(SpotifyCommand):
    def action(self):
        self.render_resource(self.spotify.find_artist(' '.join(self.args), self._get_id()), ArtistPresenter,
                             lang.msg('404_called', 'artist', ' '.join(self.args)))

    def _keyboard_buttons(self, data):
        return [{"text": lang.msg('view_albums'), "callback_data": utils.build_cmd('album', {'p': data['id']})}] + super()._keyboard_buttons(data)


class AlbumCommand(SpotifyCommand):
    def action(self):
        self.render_resource(self.spotify.find_album(' '.join(self.args), self._get_id()), AlbumPresenter, lang.msg('404_called', 'album', ' '.join(self.args)))

    def parent_action(self, id):
        self.render_resource(self.spotify.artist_albums(id, limit=ITEMS_PER_PAGE, offset=self.get_var('offset', 0)), AlbumsPresenter, lang.msg('404'))

    def _keyboard_buttons(self, data):
        return [{"text": lang.msg('view_tracks'), "callback_data": utils.build_cmd('track', {'p': data['id']})}] + super()._keyboard_buttons(data)


class TrackCommand(SpotifyCommand):
    def action(self):
        self.render_resource(self.spotify.find_track(' '.join(self.args), self._get_id()), TrackPresenter, lang.msg('404_called', 'track', ' '.join(self.args)))

    def parent_action(self, id):
        self.render_resource(self.spotify.album_tracks(id, limit=ITEMS_PER_PAGE, offset=self.get_var('offset', 0)), TracksPresenter, lang.msg('404'))
