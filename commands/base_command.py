import utils


class Message:
    def __init__(self, msg):
        self._msg = msg
        tokens = msg['text'].split()
        self.gate = tokens[0].lower()[0]
        self.command = tokens[0].lower()[1:] if self.gate == '/' else None
        self.args = tokens[1:]
        self.context = msg['context'] if 'context' in msg else None
        self.sender_id = msg['from']['id']
        self.sender_name = msg['from']['first_name']
        self.chat_id = msg['chat']['id']

    def has_context(self): return self.context is not None

    def __str__(self) -> str: return "command: {}\narguments: {}".format(self.command, self.args)


class BaseCommand:
    def __init__(self, handler, message):
        """
        :type message: Message
        :param handler:
        :type handler: telepot.helper.ChatHandler
        """
        self.handler = handler
        self.message = message

    def execute(self):
        pass

    def msg(self, text, **kwargs):
        if self.message.has_context() and self._is_edit():
            self.handler.bot.editMessageText(self.message.context, text, parse_mode='markdown', **kwargs)
        else:
            self.handler.sender.sendMessage(text, parse_mode='markdown', **kwargs)

    def sender(self): return self.handler.sender

    def build_keyboard(self, data): return utils.build_keyboard(self._keyboard_buttons(data))

    def _keyboard_buttons(self, data): return []

    def get_var(self, key='i', default=None, format=str):
        return utils.extract_var(self.message.args, key, default, format)

    def _is_edit(self): return False

    @property
    def args(self): return self.message.args
