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
              5: 'friend = "David"'}
    # inp = inputs[5]
    # with open('if_statement_tester.py', 'r') as file:
    #     inp = file.read()
    # with open("for_loop_statement_tester.py", 'r') as file:
    #     inp = file.read()

    paths = [
        "for_loop_tester_statement_invalid.py"
    ]
    for path in paths:
        with open(path, 'r') as file:
            inp = file.read()
        input_stream = InputStream(inp)
        print(f'The input is:\n"\n{inp}\n"')
        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()

        visitor = MyExprVisitor()
        res = visitor.visit(tree)  # Evaluate the expression

        # print(res)

if __name__ == '__main__':
    main()
