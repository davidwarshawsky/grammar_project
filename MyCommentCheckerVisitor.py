from CommentCheckerParser import CommentCheckerParser
from CommentCheckerVisitor import CommentCheckerVisitor


class MyCommentCheckerVisitor(CommentCheckerVisitor):
    def __init__(self):
        super(MyCommentCheckerVisitor, self).__init__()
        # self.stack = []  # Stack to evaluate the expression

    # Visit a parse tree produced by CommentCheckerVisitor#prog.
    def visitProg(self, ctx: CommentCheckerVisitor.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by CommentCheckerVisitor#infixExpr.
    def visitInfixExpr(self, ctx: CommentCheckerVisitor.InfixExprContext):
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

    # Visit a parse tree produced by CommentCheckerVisitor#numberExpr.
    def visitNumberExpr(self, ctx: CommentCheckerVisitor.NumberExprContext):
        c = int(str(ctx.INT()))  # Found a number, just insert to stack
        self.stack.append(c)
        return c

    # Visit a parse tree produced by CommentCheckerVisitor#parensExpr.
    def visitParensExpr(self, ctx: CommentCheckerVisitor.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

    # Visit a parse tree produced by CommentCheckerParser#logicalExpr.
