import re

sanitize_words = [
    'bonus',
    'demo',
    'edit',
    'explicit',
    'extended',
    'feat',
    'mono',
    'remaster',
    'stereo',
    'version'
]


def _compile_re( expression):
    meta_words = '|'.join(sanitize_words)
    expression = expression.replace('META_WORDS_HERE', meta_words)
    return re.compile(expression, re.IGNORECASE)


after_delimiter = _compile_re(r"([\-,;/])([^\-,;/])*(META_WORDS_HERE).*")
inside_brackets = _compile_re(r"([\(\[][^)\]]*?(META_WORDS_HERE)[^)\]]*?[\)\]])")


def sanitize_title(title):
    title = re.sub(inside_brackets, "", title)
    title = re.sub(after_delimiter, "", title)
    return title.strip()