import telepot
import commands


class BlackSabboth(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(BlackSabboth, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        if not msg.get("text"): return

        tokens = msg['text'].split()
        command = tokens[0].lower()[1:]
        args = tokens[1:]

        context = msg['context'] if 'context' in msg else None
        if command in commands.routes: commands.routes[command](self, command, args, context).execute()
        else: self.on_unknown_intent()

    def on_unknown_intent(self):
        self.sender.sendMessage('What are you talking about!?')

    def on_callback_query(self, msg):
        msg['text'] = msg['data']
        msg['context'] = telepot.message_identifier(msg['message'])
        self.on_chat_message(msg)
