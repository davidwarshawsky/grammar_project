import sys

from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor



def main(argv):
    test_cases = [
        # Arithmetic expressions
        "10 - 2 * 2 / 4",
        "10 - (2 * 2 / 4)",
        "10 - 12 * (2 / 4) + 2 * 9 + 171",
        "1 + 12 * (123 + 1234) - 12345 / 123456",
        "(1 + 2) - (2 * 3) / (2 * 9 - 1) * 19",

        # Exponentiation
        "2 ^ 2 * 3 + 2 + 1",
        "2 ^ 2 + (3 * 2)",
        "(1 - 3) * 2 ^ (2 ^ (3 - 10)) ^ 2 - 9 / 10 ^ 2",
        "3 ^ 2 ^ 3 * 3 + 2 - 8 + (2 + 3 * 10)",
        "3 ^ (5 - 10) / 18 * 7999",

        # Logical expressions
        "True and False",
        "True or False",
        "True and False or True",
        "True or False and True",

        # Lambda functions

        # Comments
        "1 + 2 # This is a comment",


    ]

    for i, test_case in enumerate(test_cases):
        lexer = ExprLexer(InputStream(test_case))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        res = MyExprVisitor().visitProg(tree)
        print(f"Test Case {i+1}: {test_case} = {res}")

if __name__ == '__main__':
    main(sys.argv)
