import re

from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup


def build_keyboard(buttons):
    return InlineKeyboardMarkup(inline_keyboard=_process_buttons(buttons))


def _process_buttons(buttons, level=0):
    ret = []
    for button in buttons:
        if type(button) is dict:
            ret.append(InlineKeyboardButton(**button))
        else: ret.append(_process_buttons(button, level + 1))
    if len(ret) > 0 and type(ret[0]) != list and level == 0: return [ret]
    return ret


def extract_var(tokens, key, default=None, format=str):
    if len(tokens) == 0: return default
    for arg in tokens:
        match = re.match('(\${0})*(\${0})\w+'.format(key), arg)
        if match is not None: return format(match.string[len(key) + 1:-(len(key) + 1)])
    return default


def pack_var(key, value):
    return '${0}{1}${0}'.format(key, value)


def build_cmd(command, vars=None, args=None):
    if args is None: args = []
    if vars is None: vars = []
    vars = [pack_var(key, value) for key, value in vars.items()]
    return '/{} {} {}'.format(command, ' '.join(vars), ' '.join(args))


def filter_non_vars(tokens):
    ret = []
    for arg in tokens:
        if re.match('(\$)*(\$)\w+', arg) is None: ret.append(arg)
    return ret
