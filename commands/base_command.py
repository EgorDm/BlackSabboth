class BaseCommand:
    def __init__(self, handler, command, args):
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

        print(f"command: {type(self).__name__}\narguments: {args}")

    def execute(self):
        pass

    def msg(self, text):
        self.handler.sender.sendMessage(text)
