from TestParser import TestParser
from TestVisitor import TestVisitor
from operations import combinations

class MyTestVisitor(TestVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()

    def check_combination(self, op, a, b):
        valid_combinations = combinations[op]
        for combination in valid_combinations:
            if (a, b) == (combination[0], combination[1]) or (b, a) == (combination[0], combination[1]):
                return combination[2]
        raise ValueError(f"Invalid operation: {a} {op} {b}")

    def check_ops(self, ctx):
        a = self.visit(ctx.left)
        b = self.visit(ctx.right)
        return self.check_combination(ctx.op.text, a, b)

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        # Chnage the try except finally to say the program is correctly made
        try:
            return self.visit(ctx.expr())  # Visit the expression
        except ValueError as e:
            print(e)
        finally:
            print("Data Type:" + self.visit(ctx.expr()))
            print("Program is correctly made")
        # try:
        #     return self.visit(ctx.expr())  # Just visit the self expression
        # except ValueError as e:
        #     print(e)
        # finally:

    def visitOrExpression(self, ctx: ExprParser.OrExpressionContext):
        return self.check_ops(ctx)

    def visitAndExpression(self, ctx: ExprParser.AndExpressionContext):
        return self.check_ops(ctx)

    def visitCompExpression(self, ctx: ExprParser.CompExpressionContext):
        return self.check_ops(ctx)

    def visitBitOrExpression(self, ctx: ExprParser.BitOrExpressionContext):
        return self.check_ops(ctx)

    def visitBitXorExpression(self, ctx: ExprParser.BitXorExpressionContext):
        return self.check_ops(ctx)

    def visitBitAndExpression(self, ctx: ExprParser.BitAndExpressionContext):
        return self.check_ops(ctx)

    def visitBitShiftExpression(self, ctx: ExprParser.BitShiftExpressionContext):
        return self.check_ops(ctx)

    def visitAddSubExpression(self, ctx: ExprParser.AddSubExpressionContext):
        return self.check_ops(ctx)

    def visitMultDivExpression(self, ctx: ExprParser.MultDivExpressionContext):
        return self.check_ops(ctx)

        # Visit a parse tree produced by ExprParser#rightAssociativePowExpr.

    def visitRightAssociativePowExpression(self, ctx: ExprParser.RightAssociativePowExpressionContext):
        a = self.visit(ctx.unaryExpr())  # Evaluate the unary expression
        if ctx.op:
            b = self.visit(ctx.powExpr())  # If there's a power operation, evaluate the right expression
            result_data_type = self.check_combination(ctx.op.text, a, b)
            return result_data_type
        else:
            return a

    def visitIfStatementExpression(self, ctx: ExprParser.If_statement_expressionContext):
        # Evaluate the expression for 'if'
        if_expr_result = self.visit(ctx.expr(0))
        # Check if the result is a bool or ID
        if if_expr_result not in ['BOOL', 'ID']:
            raise ValueError(f"Invalid condition in if statement: {if_expr_result}")

        # Evaluate the expressions for 'elif'
        for i in range(1, len(ctx.expr()), 2):
            elif_expr_result = self.visit(ctx.expr(i))
            # Check if the result is a bool or ID
            if elif_expr_result not in ['BOOL', 'ID']:
                raise ValueError(f"Invalid condition in elif statement: {elif_expr_result}")

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpression(self, ctx: ExprParser.ParensExpressionContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr.

    # Visit a parse tree produced by ExprParser#data_structures.
    def visitData_structures(self, ctx: ExprParser.Data_structuresContext):
        # Return the appropriate data type based on the context
        if ctx.int_():
            return 'INT'
        elif ctx.float_():
            return 'FLOAT'
        elif ctx.bool_():
            return 'BOOL'
        elif ctx.string():
            return 'STRING'
        elif ctx.tuple_():
            return 'TUPLE'
        elif ctx.list_():
            return 'LIST'
        elif ctx.dict_():
            return 'DICT'
        elif ctx.none():
            return 'NONE'
        elif ctx.ID():
            return 'ID'
        elif ctx.set_():
            return 'SET'

    # Visit a parse tree produced by ExprParser#dict.
    def visitDict(self, ctx: ExprParser.DictContext):
        return 'DICT'

    # Visit a parse tree produced by ExprParser#set.
    def visitSet(self, ctx: ExprParser.SetContext):
        return 'SET'

    # Visit a parse tree produced by ExprParser#list.
    def visitList(self, ctx: ExprParser.ListContext):
        return 'LIST'

    def visitAssignmentExpression(self, ctx: ExprParser.AssignmentExpressionContext):
        return self.visit(ctx.expr())
