import os
import telepot
from telepot.delegate import create_open, pave_event_space, per_chat_id
import commands


class AgentHandler(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(AgentHandler, self).__init__(*args, **kwargs)

    def on_message(self, msg):
        if not msg.get("text"): return

        tokens = msg['text'].split()
        command = tokens[0].lower()[1:]
        args = tokens[1:]

        if command in commands.routes: commands.routes[command](self, command, args).execute()
        else: self.on_unknown_intent()

    def on_unknown_intent(self):
        self.sender.sendMessage('What are you talking about!?')


class BlackSabboth(telepot.DelegatorBot):
    def __init__(self):
        super(BlackSabboth, self).__init__(os.environ.get("TELEGRAM_KEY"), [
            pave_event_space()(per_chat_id(), create_open, AgentHandler, timeout=20),
        ])
