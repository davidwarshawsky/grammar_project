# Generated from CommentChecker.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommentCheckerParser import CommentCheckerParser
else:
    from CommentCheckerParser import CommentCheckerParser

# This class defines a complete generic visitor for a parse tree produced by CommentCheckerParser.

class CommentCheckerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommentCheckerParser#file.
    def visitFile(self, ctx:CommentCheckerParser.FileContext):
        return self.visitChildren(ctx)



# del CommentCheckerParser 