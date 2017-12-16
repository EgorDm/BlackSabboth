import commands


class HelpCommand(commands.BaseCommand):
    help_lines = [
        'Well, hello there! I am the living incarnation of Dio!',
        'I am here to help you accesing your music and making it more social.\n',
        'Talk to me by giving following commands\n',
        '*Music commands*',
        '/artist _<name>_ - View information about given artist',
        '/album _<name>_ - View information about given album',
        '/track _<name>_ - View information about given track. *Also gives a preview*',
        'You have to fill in the name of artist, album or track. It doesnt have to be exactly right. I can search :)'
        '\n\n*Game commands*\n'
        '/game _<source>_ _<name>_ - Starts a game. You have to specify *source* where you can choose out of [artist, album, track] and name of the given source.',
        '/stop - Stops the game',
        '/skip - Skips the current question. *Its cheating to use it!*',
        '/stats - Give statisting of the players in game'
        '/guess - A command to manually give a guess. *Use inline keyboard instead*',
        '/help - Give this message\n',
        '*Game rules*',
        'I pick lyrics of your given source like artist or album. Then I give you a few lines and you have to choose what comes next.'
    ]

    def execute(self):
        self.msg('\n'.join(self.help_lines))
