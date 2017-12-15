import utils


class BaseCommand:
    def __init__(self, handler, command, args, context=None):
        """
        :type command:
        :param handler:
        :type handler: telepot.helper.ChatHandler
        :param args:
        :type args:
        """
        self.handler = handler
        self.command = command
        self.args = args
        self.context = context

        print(f"command: {type(self).__name__}\narguments: {args}")

    def execute(self):
        pass

    def msg(self, text, **kwargs):
        if self.context is not None and self._is_edit():
            self.handler.bot.editMessageText(self.context, text, parse_mode='markdown', **kwargs)
        else:
            self.handler.sender.sendMessage(text, parse_mode='markdown', **kwargs)

    def sender(self): return self.handler.sender

    def build_keyboard(self, data): return utils.build_keyboard(self._keyboard_buttons(data))

    def _keyboard_buttons(self, data): return []

    def get_var(self, key='i', default=None, format=str):
        return utils.extract_var(self.args, key, default, format)

    def _is_edit(self): return False
