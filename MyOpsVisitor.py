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
                right = self.visit(ctx.expr()[-1])
                print("ctx.expr() length: " + str(len(ctx.expr())))
                # print text of ctx.expr()[-1]
                print(ctx.expr()[-1].getText())
                print(f"right = {right}")
                left = self.visit(ctx.data_structures())
                print(f"left = {left}")
                print(ctx.data_structures().getText())

            else:
                # For all other operators, visit the left child before the right child
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
            for combination in combinations[op]:
                if (left, right) == combination[:2]:
                    return combination[2]
                elif (right, left) == combination[:2]:
                    return combination[2]
                else:
                # If the operation is invalid, raise an error
                    raise TypeError(f'unsupported operand type(s) for {op}: {left} and {right}')
        # check the data structure if it is a dictionary
        else:
            data_structure = self.visit(ctx.data_structures())
            if data_structure == 'DICT':
            # Check if the key of the dictionary is an immutable data type
                self.visitDict_(ctx.dict_())
            return data_structure
    
    def visitDict_(self, ctx:OpsParser.DictContext):
        # Iterate over all children of the dict context
        for i in range(0, len(ctx.children)):
            # Check if the child is a key (it should be an instance of Data_structuresContext)
            if isinstance(ctx.getChild(i), OpsParser.Data_structuresContext):
                key_type = self.visit(ctx.getChild(i))
                if key_type not in ['INT', 'FLOAT', 'STRING', 'BOOL', 'TUPLE', 'NONE']:
                    raise TypeError(f"Mutable types are not allowed as keys: {key_type}")
        return 'DICT'
    def visitData_structures(self, ctx:OpsParser.Data_structuresContext):
        if ctx.INT() is not None:
            return 'INT'
        elif ctx.FLOAT() is not None:
            return 'FLOAT'
        elif ctx.BOOL() is not None:
            return 'BOOL'
        elif ctx.STRING() is not None:
            return 'STRING'
        elif ctx.TUPLE() is not None:
            return 'TUPLE'
        elif ctx.list_() is not None:
            return 'LIST'
        elif ctx.dict_() is not None:
            return 'DICT'
        elif ctx.NONE() is not None:
            return 'NONE'
        elif ctx.set_() is not None:
            return 'SET'


def main():
    # The input expression
    input_expr = '2 * {"hello":"david"} / 5 * 2 + 3 ** 2 / 2'
    input_expr_2 = '["hello"] * 3'
    input_expr_3 = '[x for x in [1,2,3,4] for y in [1,2,3]]'
    input_expr_4 = '{1001: 1001 > 1000, 10001: 10001 > 1000, 100001: 100001 > 1000, 1000001: 1000001 > 1000, 10000001: 10000001 > 1000}'
    input_expr_5 = '{{"hi":"there"}:1 for x in [1,2,3,4]}'
    input_expr_6 = '["hello"] * 2.3'
    input_expr_7 = '{[]:1}'
    input_expr_8 = '2 ** 3 ** 2'
    input_expr_9 = '"hello" ** 3 ** 2'
    # Create the lexer and parser
    lexer = OpsLexer(InputStream(input_expr_8))
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


# def example():
#        print("hello ")
#     print("world")
# print("Hello")
# example()

# def example2():
#     print("hello")
#     print("world")
# print("Hello")
# example()