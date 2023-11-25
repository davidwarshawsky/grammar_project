from antlr4 import *
import sys
from CommentCheckerLexer import CommentCheckerLexer
from CommentCheckerParser import CommentCheckerParser
from CommentCheckerVisitor import CommentCheckerVisitor
from antlr4.error.ErrorListener import ErrorListener

class MyCommentCheckerVisitor(CommentCheckerVisitor):
    def visitFile(self, ctx:CommentCheckerParser.FileContext):
        if ctx.COMMENTLINE():
            print("There was a comment in this input.\n")
        return super().visitFile(ctx)

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if 'COMMENTLINE' in msg:
            print("There was no comment in this file.\n")



def main(argv):
    inputs = [
        "# This is a comment.",
        "    # This is a comment",
        "    #4his is a comment",
        "This is not a comment",
        "This is not a comment # This is a comment."]
    
    for test_input in inputs:
        print("Input: {}\n".format(test_input))
        # Create an input stream from standard input
        input_stream = InputStream(test_input)

        # Create a lexer that feeds off of the input stream
        lexer = CommentCheckerLexer(input_stream)

        # Create a buffer of tokens pulled from the lexer
        token_stream = CommonTokenStream(lexer)

        # Create a parser that feeds off the token stream
        parser = CommentCheckerParser(token_stream)

        lexer.removeErrorListeners()
        parser.removeErrorListeners()
        # Create an instance of your custom error listener
        myErrorListener = MyErrorListener()

        # Add your custom error listener to the lexer and parser
        lexer.addErrorListener(myErrorListener)
        parser.addErrorListener(myErrorListener)

        # Start parsing from the file rule
        tree = parser.file_()

        # Create a visitor instance
        visitor = MyCommentCheckerVisitor()

        # Visit the parse tree
        visitor.visitFile(tree)

if __name__ == '__main__':
    main(sys.argv)
