from antlr4 import *
import sys
from CommentCheckerLexer import CommentCheckerLexer
from CommentCheckerParser import CommentCheckerParser
from CommentCheckerVisitor import CommentCheckerVisitor

class MyCommentCheckerVisitor(CommentCheckerVisitor):
    def visitFile(self, ctx:CommentCheckerParser.FileContext):
        if ctx is None:
            raise Exception("There was no comment in this file.")
        return super().visitFile(ctx)

def main(argv):
    test_input = " #     This is a comment."
    # Create an input stream from standard input
    input_stream = InputStream(test_input)

    # Create a lexer that feeds off of the input stream
    lexer = CommentCheckerLexer(input_stream)

    # Create a buffer of tokens pulled from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = CommentCheckerParser(token_stream)

    # Start parsing from the file rule
    tree = parser.file_()

    # Create a visitor instance
    visitor = MyCommentCheckerVisitor()

    # Visit the parse tree
    visitor.visitFile(tree)

if __name__ == '__main__':
    main(sys.argv)
