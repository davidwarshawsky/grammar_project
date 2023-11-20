from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx: ExprParser.InfixExprContext):
        self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        self.visit(ctx.right)  # Evaluate the right expression and push to stack
        b = self.stack.pop()  # Why is ‘b’ the first popped item?
        a = self.stack.pop()
        c = None

        if ctx.OP_ADD():
            c = a + b
        elif ctx.OP_SUB():
            c = a - b
        elif ctx.OP_MUL():
            c = a * b
        elif ctx.OP_DIV():
            c = a / b
        elif ctx.OP_POW():
            c = a ** b

        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx: ExprParser.NumberExprContext):
        c = int(str(ctx.INT()))  # Found a number, just insert to stack
        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

    # Visit a parse tree produced by ExprParser#logicalExpr.
