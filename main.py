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

    loginput1 = InputStream("true and false or true")
    loginput2 = InputStream("true and false or not true")
    loginput3 = InputStream("true and false or not true and true")
    loginput4 = InputStream("true and false or not true and true or true")
    loginput5 = InputStream("true and false or not true and true or true and false")

    lambdaInput1 = InputStream("lambda x: x + 1")
    lambdaInput2 = InputStream("lambda x, y: x + y")
    lambdaInput3 = InputStream("lambda x, y: x + y + 1")
    lambdaInput4 = InputStream("lambda x, y, z: x + y + z")

    commentInput1 = InputStream("1 + 2 # This is a comment")
    commentInput2 = InputStream("1 + 2 # This is a comment\n3 + 4")
    commentInput3 = InputStream("1 + 2 # This is a comment\n3 + 4 # This is a comment")
    commentInput4 = InputStream("1 + 2 # This is a comment\n3 + 4 # This is a comment\n5 + 6")

    StringInput1 = InputStream('"This is a string"')
    StringInput2 = InputStream('"This is a string" + "This is another string"')

    listInput1 = InputStream("[1, 2, 3]")
    listInput2 = InputStream("[1, 2, 3] + [4, 5, 6]")

    SetInput1 = InputStream("{1, 2, 3}")
    tupleInput1 = InputStream("(1, 2, 3)")


    lexer = ExprLexer(powinput1)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    res = MyExprVisitor().visitProg(tree)  # Evaluate the expression

    print(powinput1, '=', res)


if __name__ == '__main__':
    main(sys.argv)