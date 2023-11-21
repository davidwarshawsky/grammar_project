# Generated from CommentChecker.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,28,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,4,1,17,8,1,11,1,12,1,18,1,1,1,1,1,2,5,2,24,8,2,
        10,2,12,2,27,9,2,0,0,3,1,1,3,2,5,3,1,0,2,2,0,9,9,32,32,2,0,10,10,
        13,13,30,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,16,1,
        0,0,0,5,25,1,0,0,0,7,9,3,3,1,0,8,10,5,35,0,0,9,8,1,0,0,0,10,11,1,
        0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,3,5,2,0,14,
        2,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,0,17,18,1,0,0,0,18,16,1,0,0,
        0,18,19,1,0,0,0,19,20,1,0,0,0,20,21,6,1,0,0,21,4,1,0,0,0,22,24,8,
        1,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,
        6,1,0,0,0,27,25,1,0,0,0,4,0,11,18,25,1,6,0,0
    ]

class CommentCheckerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENTLINE = 1
    WS = 2
    ANY = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "COMMENTLINE", "WS", "ANY" ]

    ruleNames = [ "COMMENTLINE", "WS", "ANY" ]

    grammarFileName = "CommentChecker.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


