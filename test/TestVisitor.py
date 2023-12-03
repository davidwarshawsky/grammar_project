# Generated from Test.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete generic visitor for a parse tree produced by TestParser.

class TestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestParser#prog.
    def visitProg(self, ctx:TestParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#statement.
    def visitStatement(self, ctx:TestParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:TestParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#assignment.
    def visitAssignment(self, ctx:TestParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#ifStatement.
    def visitIfStatement(self, ctx:TestParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#whileStatement.
    def visitWhileStatement(self, ctx:TestParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#forStatement.
    def visitForStatement(self, ctx:TestParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#printStatement.
    def visitPrintStatement(self, ctx:TestParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#returnStatement.
    def visitReturnStatement(self, ctx:TestParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#block.
    def visitBlock(self, ctx:TestParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#expression.
    def visitExpression(self, ctx:TestParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#orExpression.
    def visitOrExpression(self, ctx:TestParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#andExpression.
    def visitAndExpression(self, ctx:TestParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#compExpression.
    def visitCompExpression(self, ctx:TestParser.CompExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#addExpression.
    def visitAddExpression(self, ctx:TestParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#multExpression.
    def visitMultExpression(self, ctx:TestParser.MultExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#unaryExpression.
    def visitUnaryExpression(self, ctx:TestParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:TestParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#literal.
    def visitLiteral(self, ctx:TestParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:TestParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#parameterList.
    def visitParameterList(self, ctx:TestParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#functionCall.
    def visitFunctionCall(self, ctx:TestParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#argumentList.
    def visitArgumentList(self, ctx:TestParser.ArgumentListContext):
        return self.visitChildren(ctx)



del TestParser