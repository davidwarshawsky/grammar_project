from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
        self.variables = {}  # Dictionary to store variables
        self.variables_list = []
        self.type_value_dict = {}
        # for DEF parametres
        self.buffer_pare = {}
        # for -- / ++ operators
        self.operator_pare = {}
        # dor IF / WHILE operators
        self.operator = False

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        if ctx.expr():  # Check if there are any expressions
            return self.visit(ctx.expr(0))  # Visit the first expression

    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx):
        if ctx.INT():
            c = int(str(ctx.INT()))
        elif ctx.FLOAT():
            c = float(str(ctx.FLOAT()))

        self.stack.append(c)

        return c

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

    # Visit a parse tree produced by ExprParser#

    # Override visitStringExpr
    def visitStringExpr(self, ctx):
        self.stack.append(str(ctx.STRING().getText()))
        return str(ctx.STRING().getText())

    # Override visitVariableExpr
    def visitVariableExpr(self, ctx):
        variable_name = ctx.ID().getText()
        # You may want to handle variable lookup and push its value onto the stack here

        self.stack.append(variable_name)

    # Override visitInfixExpr for binary operations
    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx):
        self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        self.visit(ctx.right)  # Evaluate the right expression and push to stack

        b = self.stack.pop()  # Why is ‘b’ the first popped item?
        a = self.stack.pop()
        c = None

        if ctx.OP_POW():
            c = a ** b

        elif ctx.OP_ADD():
            c = a + b
        elif ctx.OP_SUB():
            c = a - b
        elif ctx.OP_MUL():
            c = a * b
        elif ctx.OP_DIV():
            c = a / b
        elif ctx.OP_MOD():
            c = a % b
        elif ctx.OP_FLOOR_DIV():
            c = a // b

        self.stack.append(c)
        return c

    def visitAndExpr(self, ctx: ExprParser.AndExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        b = self.stack.pop()
        a = self.stack.pop()
        c = a and b

        if a != b:
            c = False

        self.stack.append(c)
        return c

    def visitOrExpr(self, ctx: ExprParser.OrExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        b = self.stack.pop()
        a = self.stack.pop()
        c = a or b
        if a != b:
            c = True

        self.stack.append(c)
        return c

    def visitCommentExpr(self, ctx: ExprParser.CommentExprContext):
        pass

    def visitStringExpr(self, ctx):
        string_literal = str(ctx.STRING().getText())  # Get the raw string with quotes
        # Remove the quotes at the beginning and end of the string
        string_value = string_literal[1:-1]
        self.stack.append(string_value)
        return string_value


