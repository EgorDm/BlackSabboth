from math import floor, ceil

import lang
import utils

ITEMS_PER_PAGE = 6


class SpotifyPresenter:
    def present(self, resource, command, bot):
        """
        :param resource:
        :type resource:
        :param command:
        :type command: SpotifyCommand
        :param bot:
        :type bot:
        :return:
        :rtype:
        """
        pass


class ArtistPresenter(SpotifyPresenter):
    def present(self, resource, command, bot):
        if len(resource['images']) > 0:  bot.sendPhoto(command.spotify.pick_photo(resource['images']))
        genres = ', '.join(resource['genres'])
        message = lang.msg('artist', resource['name'], resource['followers']['total'], genres)

        command.msg(message, reply_markup=command.build_keyboard(resource))


class AlbumPresenter(SpotifyPresenter):
    def present(self, resource, command, bot):
        if len(resource['images']) > 0:  bot.sendPhoto(command.spotify.pick_photo(resource['images']))
        genres = ', '.join(resource['genres'])
        artists = ', '.join([artist['name'] for artist in resource['artists']])
        message = lang.msg('album', resource['name'], resource['release_date'], artists, genres, len(resource['tracks']))

        command.msg(message, reply_markup=command.build_keyboard(resource))


class CollectionPresenter(SpotifyPresenter):
    def present(self, resource, command, bot):
        offset = int(command.get_var("offset", 0))
        kb_items = [self.build_button(item) for item in resource[1]]

        # TODO inefficient af
        next_cmd = utils.build_cmd(self.get_command(), {'p': command.get_var("p"), 'offset': int(command.get_var("offset", 0)) + ITEMS_PER_PAGE, 'rep': 1})
        prev_cmd = utils.build_cmd(self.get_command(), {'p': command.get_var("p"), 'offset': int(command.get_var("offset", 0)) - ITEMS_PER_PAGE, 'rep': 1})
        if offset >= ITEMS_PER_PAGE: kb_items = [[{"text": lang.msg('previous_page'), "callback_data": prev_cmd}]] + kb_items
        if offset + ITEMS_PER_PAGE < resource[0]: kb_items.append([{"text": lang.msg('next_page'), "callback_data": next_cmd}])

        command.msg(lang.msg('list_items', floor(offset / ITEMS_PER_PAGE) + 1, ceil(resource[0] / ITEMS_PER_PAGE)), reply_markup=utils.build_keyboard(kb_items))

    def build_button(self, item): pass

    def get_command(self): pass


class AlbumsPresenter(CollectionPresenter):

    def build_button(self, item): return [{"text": item['name'], "callback_data": utils.build_cmd('album', {'i': item['id']})}]

    def get_command(self): return 'album'


class TrackPresenter(SpotifyPresenter):
    def present(self, resource, command, bot):
        artists = ', '.join([artist['name'] for artist in resource['artists']])
        message = lang.msg('track', resource['name'], artists, resource['duration_ms'] / 60000)

        command.msg(message, reply_markup=command.build_keyboard(resource))
        if 'preview_url' in resource: bot.sendAudio(resource['preview_url'], caption='Preview', duration=30, title=resource['name'], performer=artists)


class TracksPresenter(CollectionPresenter):
    def build_button(self, item): return [{"text": item['name'], "callback_data": utils.build_cmd('track', {'i': item['id']})}]

    def get_command(self): return 'track'
