import commands


class GreetCommand(commands.BaseCommand):
    def execute(self):
        super().execute()
        self.msg('Grreeetings! ☠️')