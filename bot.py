import telepot
from telepot.delegate import include_callback_query_chat_id, pave_event_space, per_chat_id, create_open
import commands
from commands import Message
from logic import SpotifyController
from logic.lyric_game_controller import LyricGameController


class TheManager(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(TheManager, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text': return

        message = Message(msg)
        if message.command is not None and message.command in commands.routes: return commands.routes[message.command](self, message).execute()
        # if message.gate == '/': self.on_unknown_intent()

    def on_unknown_intent(self):
        self.sender.sendMessage('What are you talking about!?')

    def on_callback_query(self, msg):
        msg['chat'] = msg['message']['chat']
        msg['text'] = msg['data']
        msg['context'] = telepot.message_identifier(msg['message'])
        self.on_chat_message(msg)


class BlackSabboth(telepot.DelegatorBot):
    def __init__(self, token):
        super().__init__(token, [
            include_callback_query_chat_id(
                pave_event_space())(
                per_chat_id(), create_open, TheManager, timeout=10),
        ])

        self.spotify_controller = SpotifyController(self)
        self.game_controller = LyricGameController(self)
