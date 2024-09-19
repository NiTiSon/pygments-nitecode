"""A Pygments lexer for NiteCode language."""
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("NiteCodeLexer",)


class NiteCodeLexer(RegexLexer):
    name = 'NiteCode'
    aliases = ['nite', 'nitecode']
    filenames = ['*.nite', '*.nitecode']
    mimetypes = ['text/nitecode']

    tokens = {
        'root': [
            (r'^([a-f\d]{8}\:)([ \t]*)', bygroups(String, Whitespace), 'address'),
            (r'^(\s*)(::.*?)$', bygroups(Whitespace, Comment.Single)),
            (r'^.+?$', Error),  # invalid
            (r'.+?$', Comment.Single)
        ],

        'address': [
            (r'([ \t]*)(?:(\:)|$)', bygroups(Whitespace, String), '#pop'),
            (r'[\da-f]{1}', Number, 'byte'),
            (r'[ \t]', Whitespace),
            (r'.+$', Error, '#pop')  # invalid
        ],

        'byte': [
            (r'[\da-f]{1}', Text, '#pop'),
            (r'.', Error, '#pop')  # invalid
        ]
    }