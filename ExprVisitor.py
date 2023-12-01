# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#orExpression.
    def visitOrExpression(self, ctx:ExprParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#andExprPass.
    def visitAndExprPass(self, ctx:ExprParser.AndExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#andExpression.
    def visitAndExpression(self, ctx:ExprParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#compExprPass.
    def visitCompExprPass(self, ctx:ExprParser.CompExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#compExpression.
    def visitCompExpression(self, ctx:ExprParser.CompExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitOrExprPass.
    def visitBitOrExprPass(self, ctx:ExprParser.BitOrExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitOrExpression.
    def visitBitOrExpression(self, ctx:ExprParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitXorExprPass.
    def visitBitXorExprPass(self, ctx:ExprParser.BitXorExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitAndExprPass.
    def visitBitAndExprPass(self, ctx:ExprParser.BitAndExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitXorExpression.
    def visitBitXorExpression(self, ctx:ExprParser.BitXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitAndExpression.
    def visitBitAndExpression(self, ctx:ExprParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitShiftExprPass.
    def visitBitShiftExprPass(self, ctx:ExprParser.BitShiftExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitShiftExpression.
    def visitBitShiftExpression(self, ctx:ExprParser.BitShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addExprPass.
    def visitAddExprPass(self, ctx:ExprParser.AddExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSubExpression.
    def visitAddSubExpression(self, ctx:ExprParser.AddSubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multExprPass.
    def visitMultExprPass(self, ctx:ExprParser.MultExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#powExprPass.
    def visitPowExprPass(self, ctx:ExprParser.PowExprPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multDivExpression.
    def visitMultDivExpression(self, ctx:ExprParser.MultDivExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#rightAssociativePowExpression.
    def visitRightAssociativePowExpression(self, ctx:ExprParser.RightAssociativePowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parensExpression.
    def visitParensExpression(self, ctx:ExprParser.ParensExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dataTypeExpression.
    def visitDataTypeExpression(self, ctx:ExprParser.DataTypeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:ExprParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStatementExpression.
    def visitIfStatementExpression(self, ctx:ExprParser.IfStatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#data_structures.
    def visitData_structures(self, ctx:ExprParser.Data_structuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#float.
    def visitFloat(self, ctx:ExprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bool.
    def visitBool(self, ctx:ExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx:ExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#none.
    def visitNone(self, ctx:ExprParser.NoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tuple.
    def visitTuple(self, ctx:ExprParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dict.
    def visitDict(self, ctx:ExprParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#set.
    def visitSet(self, ctx:ExprParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#list.
    def visitList(self, ctx:ExprParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_expr.
    def visitFor_expr(self, ctx:ExprParser.For_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_expr.
    def visitIf_expr(self, ctx:ExprParser.If_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_statement_expression.
    def visitIf_statement_expression(self, ctx:ExprParser.If_statement_expressionContext):
        return self.visitChildren(ctx)



del ExprParser