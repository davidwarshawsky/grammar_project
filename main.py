import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor

def main():
    inputs = {0:'"hello" *  3',
              1:'{1,2,3} * 3',
              2:'{} * 3',
              3:'(1+2+3) + 5 ** 1',
              4:'(1+2+3)',
              5: 'friend = "David"',
              6: '5',
              7: 'if 2>3:  '}
    #inp = inputs[7]
    with open('if_statement_tester.py', 'r') as file:
        inp = file.read()
    input_stream = InputStream(inp)
    print(f"User input: {inp}")
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    visitor = MyExprVisitor()
    res = visitor.visit(tree)  # Evaluate the expression

    # print(res)

if __name__ == '__main__':
    main()
