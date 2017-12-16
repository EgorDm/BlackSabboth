import commands
import lang
import utils
from logic import GameException


class LyricGameCommand(commands.BaseCommand):
    def __init__(self, handler, message):
        super().__init__(handler, message)
        self.game = handler.bot.game_controller
        self.session = self.game.sessions[self.message.chat_id] if self.message.chat_id in self.game.sessions else None

    def execute(self):
        try: self.do_logic()
        except GameException as e: return self.msg(str(e))

    def do_logic(self):
        pass


class StartGameCommand(LyricGameCommand):
    def do_logic(self):
        source_type = list(filter(lambda x: x in ['artist', 'album', 'track'], self.args))
        if len(source_type) == 0: return self.msg(lang.msg('no_source'))
        name = ' '.join(list(filter(lambda x: x not in ['artist', 'album', 'track'], self.args)))
        self.game.start_game(self.message.chat_id, source_type[0], name, self.get_var('i'))
        self.msg(lang.msg('game_started'))
        (NextLineCommand(self.handler, self.message)).execute()


class StopGameCommand(LyricGameCommand):
    def do_logic(self):
        if self.session is None: return self.msg(lang.msg('game_not_exists'))
        (StatsGameCommand(self.handler, self.message)).execute()
        self.game.stop_game(self.message.chat_id)
        self.msg(lang.msg('game_stopped'))


class GuessGameCommand(LyricGameCommand):
    def do_logic(self):
        if self.session is None: return self.msg(lang.msg('game_not_exists'))
        line = self.session.get_current_line()
        score = self.session.add_guess(self.message.sender_id, ' '.join(self.args))
        if score > 0: self.msg(lang.msg('game_guess_right', self.message.sender_name, score, line))
        else: self.msg(lang.msg('game_guess_wrong', self.message.sender_name, ' '.join(self.args), line))
        (NextLineCommand(self.handler, self.message)).execute()

    def _is_edit(self): return True


class NextLineCommand(LyricGameCommand):
    def do_logic(self):
        if self.session is None: return self.msg(lang.msg('game_not_exists'))
        self.session.randomize_line()
        lines = self.session.get_guess_lines()
        self.msg(lang.msg('game_quess', '\n'.join(lines)), reply_markup=self.build_keyboard(None))

    def _keyboard_buttons(self, data):
        ret = []
        for choice in self.session.get_choices():
            ret.append([{"text": choice, "callback_data": utils.build_cmd('guess', {}, [choice])}])
        return ret


class StatsGameCommand(LyricGameCommand):
    def do_logic(self):
        if self.session is None: return self.msg(lang.msg('game_not_exists'))

        for user_id, score in self.session.scores.items():
            print(self.handler.bot.getChatMember(self.message.chat_id, user_id))
        ret = [lang.msg('game_stat', self.handler.bot.getChatMember(self.message.chat_id, user_id)['user']['first_name'], score)
               for user_id, score in self.session.scores.items()]
        self.msg('*Stats*\n' + '\n'.join(ret))

    def _is_edit(self): return True
