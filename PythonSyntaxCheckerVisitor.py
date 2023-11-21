# Generated from PythonSyntaxChecker.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonSyntaxCheckerParser import PythonSyntaxCheckerParser
else:
    from PythonSyntaxCheckerParser import PythonSyntaxCheckerParser

# This class defines a complete generic visitor for a parse tree produced by PythonSyntaxCheckerParser.

class PythonSyntaxCheckerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonSyntaxCheckerParser#prog.
    def visitProg(self, ctx:PythonSyntaxCheckerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#variableExpr.
    def visitVariableExpr(self, ctx:PythonSyntaxCheckerParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#infixExpr.
    def visitInfixExpr(self, ctx:PythonSyntaxCheckerParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:PythonSyntaxCheckerParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#booleanExpr.
    def visitBooleanExpr(self, ctx:PythonSyntaxCheckerParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#numberExpr.
    def visitNumberExpr(self, ctx:PythonSyntaxCheckerParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#listExp.
    def visitListExp(self, ctx:PythonSyntaxCheckerParser.ListExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:PythonSyntaxCheckerParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#defExpr.
    def visitDefExpr(self, ctx:PythonSyntaxCheckerParser.DefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#parenExpr.
    def visitParenExpr(self, ctx:PythonSyntaxCheckerParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#number.
    def visitNumber(self, ctx:PythonSyntaxCheckerParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#lambda.
    def visitLambda(self, ctx:PythonSyntaxCheckerParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#funcDef.
    def visitFuncDef(self, ctx:PythonSyntaxCheckerParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#paramList.
    def visitParamList(self, ctx:PythonSyntaxCheckerParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#funcCall.
    def visitFuncCall(self, ctx:PythonSyntaxCheckerParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#argList.
    def visitArgList(self, ctx:PythonSyntaxCheckerParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#literal.
    def visitLiteral(self, ctx:PythonSyntaxCheckerParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:PythonSyntaxCheckerParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#membershipOperator.
    def visitMembershipOperator(self, ctx:PythonSyntaxCheckerParser.MembershipOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#identityOperator.
    def visitIdentityOperator(self, ctx:PythonSyntaxCheckerParser.IdentityOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#logicOperators.
    def visitLogicOperators(self, ctx:PythonSyntaxCheckerParser.LogicOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:PythonSyntaxCheckerParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#stat.
    def visitStat(self, ctx:PythonSyntaxCheckerParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#withStat.
    def visitWithStat(self, ctx:PythonSyntaxCheckerParser.WithStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#assignStat.
    def visitAssignStat(self, ctx:PythonSyntaxCheckerParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#exprStat.
    def visitExprStat(self, ctx:PythonSyntaxCheckerParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#ifStat.
    def visitIfStat(self, ctx:PythonSyntaxCheckerParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#whileStat.
    def visitWhileStat(self, ctx:PythonSyntaxCheckerParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#forStat.
    def visitForStat(self, ctx:PythonSyntaxCheckerParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#returnStat.
    def visitReturnStat(self, ctx:PythonSyntaxCheckerParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#block.
    def visitBlock(self, ctx:PythonSyntaxCheckerParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#setAssignment.
    def visitSetAssignment(self, ctx:PythonSyntaxCheckerParser.SetAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#statement.
    def visitStatement(self, ctx:PythonSyntaxCheckerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#otherStatement.
    def visitOtherStatement(self, ctx:PythonSyntaxCheckerParser.OtherStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#operator.
    def visitOperator(self, ctx:PythonSyntaxCheckerParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#setLiteral.
    def visitSetLiteral(self, ctx:PythonSyntaxCheckerParser.SetLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#dictLiteral.
    def visitDictLiteral(self, ctx:PythonSyntaxCheckerParser.DictLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#listLiteral.
    def visitListLiteral(self, ctx:PythonSyntaxCheckerParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSyntaxCheckerParser#tupleLiteral.
    def visitTupleLiteral(self, ctx:PythonSyntaxCheckerParser.TupleLiteralContext):
        return self.visitChildren(ctx)



del PythonSyntaxCheckerParser