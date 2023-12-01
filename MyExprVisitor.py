from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from operations import combinations

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()

    def check_combination(self, op, a, b):
        valid_combinations = combinations[op]
        for combination in valid_combinations:
            if (a, b) == (combination[0], combination[1]) or (b,a) == (combination[0], combination[1]):
                return combination[2]
        raise ValueError(f"Invalid operation: {a} {op} {b}")

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#addSubExpr.
    def visitAddSubExpr(self, ctx: ExprParser.AddSubExprContext):
        a = self.visit(ctx.left)  # Evaluate the left  expression
        b = self.visit(ctx.right)  # Evaluate the right expression

        result_data_type = self.check_combination(ctx.op.text, a, b)

        return result_data_type

    # Visit a parse tree produced by ExprParser#multDivExpr.
    def visitMultDivExpr(self, ctx: ExprParser.MultDivExprContext):
        a = self.visit(ctx.left)  # Evaluate the left  expression
        b = self.visit(ctx.right)  # Evaluate the right expression

        result_data_type = self.check_combination(ctx.op.text, a, b)
        
        return result_data_type
    # Visit a parse tree produced by ExprParser#rightAssociativePowExpr.
    def visitRightAssociativePowExpr(self, ctx: ExprParser.RightAssociativePowExprContext):
        a = self.visit(ctx.unaryExpr())  # Evaluate the unary expression
        if ctx.op:
            b = self.visit(ctx.powExpr())  # If there's a power operation, evaluate the right expression            
            result_data_type = self.check_combination(ctx.op.text, a, b)
            return result_data_type
        else:
            return a
    


    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
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
