# Generated from CommentChecker.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,10,2,0,7,0,1,0,4,0,4,8,0,11,0,12,0,5,1,0,1,0,1,0,0,0,1,0,0,
        0,9,0,3,1,0,0,0,2,4,5,1,0,0,3,2,1,0,0,0,4,5,1,0,0,0,5,3,1,0,0,0,
        5,6,1,0,0,0,6,7,1,0,0,0,7,8,5,0,0,1,8,1,1,0,0,0,1,5
    ]

class CommentCheckerParser ( Parser ):

    grammarFileName = "CommentChecker.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "COMMENTLINE", "WS", "ANY" ]

    RULE_file = 0

    ruleNames =  [ "file" ]

    EOF = Token.EOF
    COMMENTLINE=1
    WS=2
    ANY=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommentCheckerParser.EOF, 0)

        def COMMENTLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommentCheckerParser.COMMENTLINE)
            else:
                return self.getToken(CommentCheckerParser.COMMENTLINE, i)

        def getRuleIndex(self):
            return CommentCheckerParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = CommentCheckerParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(CommentCheckerParser.COMMENTLINE)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 7
            self.match(CommentCheckerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





