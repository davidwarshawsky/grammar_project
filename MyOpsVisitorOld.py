from antlr4 import *
from OpsLexer import OpsLexer
from OpsParser import OpsParser
from OpsVisitor import OpsVisitor
from operations import combinations
import sys



def validate_ops(ctx, lexer,stack,direction='left'):
    # # Get the type of the left operand
    left_type = ctx.left.start.type
    left_name = lexer.symbolicNames[left_type]
    # Get the type of the right operand
    right_type = ctx.right.start.type
    right_name = lexer.symbolicNames[right_type]
    print("left start: " + ctx.expr(0).start.text)
    print("right start: " + ctx.expr(1).start.text)
    left = ctx.expr.start.text
    right = ctx.right.start.text
    print(f'left: {left_name}, right: {right_name}')
    print(f"before adding to stack: {stack}")
    # Get the operator
    op = ctx.op.text if ctx.op else None
    if op:
        if direction == 'left':
            stack.append(left)
            stack.append(op)
            stack.append(right)
        if direction == 'right':
            stack.append(right)
            stack.append(op)
            stack.append(left)
        print(f"after adding to stack: {stack}")
        # If there are enough operands on the stack for the current operator
        while len(stack) >= 3:
            if direction == 'left':
                right = stack.pop()
                op = stack.pop()
                left = stack.pop()
            if direction == 'right':
                left = stack.pop()
                op = stack.pop()
                right = stack.pop()
            print(f"left: {left}, op: {op}, right: {right}")
            print(f"inside while loop: {stack}")
            # Check if the combination of left and right operand types is allowed.
            if (left_name, right_name) in combinations[op] or (right_name, left_name) in combinations[op]:
                # If the operation is valid, return the type of the result
                result = eval(f"{left} {op} {right}")
                print(result)
                stack.append(result)
                return right_name  # or left_name, depending on how you define the result type
            else:
                # If the operation is invalid, raise an error
                raise TypeError(f'unsupported operand type(s) for {op}: {left_name} and {right_name}')


def left_recurse_validate_op(visitor,ctx, lexer,stack):
        visitor.visit(ctx.expr(0))
        visitor.visit(ctx.expr(1))
        validate_ops(ctx, lexer,stack)

def right_recurse_validate_op(visitor,ctx, lexer,stack):
        stack.append(visitor.visit(ctx.expr(1)))
        stack.append(visitor.visit(ctx.expr(0)))
        validate_ops(ctx, lexer,stack,direction='right')

class MyOpsVisitor(OpsVisitor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def visitExpr(self, ctx: OpsParser.ExprContext):
        if ctx.op:
            op = ctx.op.text
            left = list(combinations.keys())
            if str(op) in left:
                left_recurse_validate_op(self,ctx, OpsLexer,self.stack)
            elif op == '**':
                right_recurse_validate_op(self,ctx, OpxLexer,self.stack)
            else:
                raise TypeError('Not a Valid Operation')
                
            self.visit(ctx.left)
            self.visit(ctx.right)
            validate_ops(ctx, self._lexer,self.stack)
        return self.visitChildren(ctx)

    def visitData_structures(self, ctx: OpsParser.Data_structuresContext):
        return self.visitChildren(ctx)
        # if ctx.INT():
        #     c = int(str(ctx.INT()))
        # elif ctx.FLOAT():
        #     c = float(str(ctx.FLOAT()))
        # elif ctx.BOOL():
        #     c = bool(ctx.BOOL().getText())
        # elif ctx.STRING():
        #     c = str(ctx.STRING().getText())
        # elif ctx.TUPLE():
        #     c = eval(ctx.TUPLE().getText())
        # elif ctx.SET():
        #     c = eval(ctx.SET().getText())
        # elif ctx.LIST():
        #     c = eval(ctx.LIST().getText())
        # elif ctx.DICT():
        #     c = eval(ctx.DICT().getText())
        # else:
        #     raise TypeError('Not a Valid Data Structure')
        # self.stack.append(c)
        # return c

    # def visitLogical_not_expr(self, ctx: OpsParser.Logical_not_exprContext):
    #     # No call to validate_ops
    #     return self.visitChildren(ctx)
    


def main():
    # Create the lexer
    lexer = OpsLexer(InputStream('2 ** 3 ** 2')) # 512

    # Create the parser
    stream = CommonTokenStream(lexer)
    parser = OpsParser(stream)

    # Parse the input
    tree = parser.prog()

    # Create the visitor
    visitor = MyOpsVisitor()  # Make sure MyOpsVisitor is defined

    # Evaluate the expression
    result = visitor.visit(tree)
    print(visitor.stack)

if __name__ == '__main__':
    main()

