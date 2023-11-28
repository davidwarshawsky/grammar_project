from antlr4 import *
from OpsLexer import OpsLexer
from OpsParser import OpsParser
from OpsVisitor import OpsVisitor
from operations import combinations

class MyExprVisitor(OpsVisitor):
    def visitProg(self, ctx:OpsParser.ProgContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx:OpsParser.ExprContext):
        if ctx.op is not None:
            op = ctx.op.text
            # For the ** operator, visit the left child before the right child
            if op == '**':
                left = self.visit(ctx.data_structures())
                right = self.visit(ctx.expr()[-1])
            else:
                # For all other operators, visit the left child before the right child
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
             # Check if the combination of left and right operand types is allowed
            if any([(left, right) in combination[:2] or (right,left) in combination[:2] for combination in combinations[op]]):
                # If the operation is valid, return the type of the result
                return combinations[op][2]  # Assuming the third value in the tuple is the result type
            else:
                # If the operation is invalid, raise an error
                raise TypeError(f'unsupported operand type(s) for {op}: {left} and {right}')
        else:
            return self.visit(ctx.data_structures())                        

    def visitData_structures(self, ctx:OpsParser.Data_structuresContext):
        if ctx.INT() is not None:
            return 'INT'
            # return int(ctx.INT().getText())
        elif ctx.FLOAT() is not None:
            return 'FLOAT'
            # return float(ctx.FLOAT().getText())
        elif ctx.BOOL() is not None:
            return 'BOOL'
            # return ctx.BOOL().getText() == 'True'
        elif ctx.STRING() is not None:
            return 'STRING'
            # return ctx.STRING().getText()[1:-1]  # Remove the quotes
        elif ctx.TUPLE() is not None:
            return 'TUPLE'
            # return tuple(self.visit(ctx.tuple_elems()))
        elif ctx.TUPLE() is not None:
            return 'TUPLE'
                # # Remove the parentheses and split the string into a list
                # items = ctx.TUPLE().getText()[1:-1].split(',')
                # # Convert the list into a tuple and return it
                # return tuple(items)
        elif ctx.SET() is not None:
            return 'SET'
            # # Remove the curly braces and split the string into a list
            # items = ctx.SET().getText()[1:-1].split(',')
            # # Convert the list into a set and return it
            # return set(items)
        elif ctx.LIST() is not None:
            return 'LIST'
            # # Remove the square brackets and split the string into a list
            # items = ctx.LIST().getText()[1:-1].split(',')
            # # Return the list
            # return items
        elif ctx.DICT() is not None:
            return 'DICT'
            # # Remove the curly braces and split the string into a list of key-value pairs
            # items = ctx.DICT().getText()[1:-1].split(',')
            # # Convert the list into a dictionary and return it
            # return dict(item.split(':') for item in items)


def main():
    # The input expression
    input_expr = '2 * {"hello":"david"} / 5 * 2 + 3 ** 2 / 2'
    input_expr_2 = '2 ** 3 ** 2'
    # Create the lexer and parser
    lexer = OpsLexer(InputStream(input_expr_2))
    stream = CommonTokenStream(lexer)
    parser = OpsParser(stream)

    # Parse the input expression
    tree = parser.prog()

    # Create the visitor
    visitor = MyExprVisitor()

    # Visit the parse tree and evaluate the expression
    result = visitor.visit(tree)

    # Print the result
    print(result)  # Outputs: 512

if __name__ == '__main__':
    main()


def example():
       print("hello ")
    print("world")
print("Hello")
example()

def example2():
    print("hello")
    print("world")
print("Hello")
example()