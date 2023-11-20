import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def main(argv):
    input = InputStream("10 - 2 * 2 / 4")
    input2 = InputStream("10 - (2 * 2 / 4)")
    input3 = InputStream("10 - 12 * (2 / 4) + 2 * 9 + 171")
    input4 = InputStream("1 + 12 * (123 + 1234) - 12345 / 123456")
    input5 = InputStream("(1 + 2) - (2 * 3) / (2 * 9 - 1) * 19")

    powinput1 = InputStream("2 ^ 2 * 3 + 2 + 1")
    powinput2 = InputStream("2 ^ 2 + (3 * 2)")
    powinput3 = InputStream("(1 - 3) * 2 ^ (2 ^ (3 - 10)) ^ 2 - 9 / 10 ^ 2")
    powinput4 = InputStream("3 ^ 2 ^ 3 * 3 + 2 - 8 + (2 + 3 * 10)")
    powinput5 = InputStream("3 ^ (5 - 10) / 18 * 7999")
    lexer = ExprLexer(powinput1)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    res = MyExprVisitor().visitProg(tree)  # Evaluate the expression

    print(powinput1, '=', res)


if __name__ == '__main__':
    main(sys.argv)