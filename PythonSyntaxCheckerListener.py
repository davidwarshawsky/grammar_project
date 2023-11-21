# Generated from PythonSyntaxChecker.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonSyntaxCheckerParser import PythonSyntaxCheckerParser
else:
    from PythonSyntaxCheckerParser import PythonSyntaxCheckerParser

# This class defines a complete listener for a parse tree produced by PythonSyntaxCheckerParser.
class PythonSyntaxCheckerListener(ParseTreeListener):

    # Enter a parse tree produced by PythonSyntaxCheckerParser#prog.
    def enterProg(self, ctx:PythonSyntaxCheckerParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#prog.
    def exitProg(self, ctx:PythonSyntaxCheckerParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#variableExpr.
    def enterVariableExpr(self, ctx:PythonSyntaxCheckerParser.VariableExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#variableExpr.
    def exitVariableExpr(self, ctx:PythonSyntaxCheckerParser.VariableExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#infixExpr.
    def enterInfixExpr(self, ctx:PythonSyntaxCheckerParser.InfixExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#infixExpr.
    def exitInfixExpr(self, ctx:PythonSyntaxCheckerParser.InfixExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:PythonSyntaxCheckerParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:PythonSyntaxCheckerParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#numberExpr.
    def enterNumberExpr(self, ctx:PythonSyntaxCheckerParser.NumberExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#numberExpr.
    def exitNumberExpr(self, ctx:PythonSyntaxCheckerParser.NumberExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:PythonSyntaxCheckerParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:PythonSyntaxCheckerParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#defExpr.
    def enterDefExpr(self, ctx:PythonSyntaxCheckerParser.DefExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#defExpr.
    def exitDefExpr(self, ctx:PythonSyntaxCheckerParser.DefExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#parenExpr.
    def enterParenExpr(self, ctx:PythonSyntaxCheckerParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#parenExpr.
    def exitParenExpr(self, ctx:PythonSyntaxCheckerParser.ParenExprContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#number.
    def enterNumber(self, ctx:PythonSyntaxCheckerParser.NumberContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#number.
    def exitNumber(self, ctx:PythonSyntaxCheckerParser.NumberContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#lambda.
    def enterLambda(self, ctx:PythonSyntaxCheckerParser.LambdaContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#lambda.
    def exitLambda(self, ctx:PythonSyntaxCheckerParser.LambdaContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#def.
    def enterDef(self, ctx:PythonSyntaxCheckerParser.DefContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#def.
    def exitDef(self, ctx:PythonSyntaxCheckerParser.DefContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#paramList.
    def enterParamList(self, ctx:PythonSyntaxCheckerParser.ParamListContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#paramList.
    def exitParamList(self, ctx:PythonSyntaxCheckerParser.ParamListContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#funcCall.
    def enterFuncCall(self, ctx:PythonSyntaxCheckerParser.FuncCallContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#funcCall.
    def exitFuncCall(self, ctx:PythonSyntaxCheckerParser.FuncCallContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#argList.
    def enterArgList(self, ctx:PythonSyntaxCheckerParser.ArgListContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#argList.
    def exitArgList(self, ctx:PythonSyntaxCheckerParser.ArgListContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#statement.
    def enterStatement(self, ctx:PythonSyntaxCheckerParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#statement.
    def exitStatement(self, ctx:PythonSyntaxCheckerParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#literal.
    def enterLiteral(self, ctx:PythonSyntaxCheckerParser.LiteralContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#literal.
    def exitLiteral(self, ctx:PythonSyntaxCheckerParser.LiteralContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:PythonSyntaxCheckerParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:PythonSyntaxCheckerParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#membershipOperator.
    def enterMembershipOperator(self, ctx:PythonSyntaxCheckerParser.MembershipOperatorContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#membershipOperator.
    def exitMembershipOperator(self, ctx:PythonSyntaxCheckerParser.MembershipOperatorContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#identityOperator.
    def enterIdentityOperator(self, ctx:PythonSyntaxCheckerParser.IdentityOperatorContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#identityOperator.
    def exitIdentityOperator(self, ctx:PythonSyntaxCheckerParser.IdentityOperatorContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#logicOperators.
    def enterLogicOperators(self, ctx:PythonSyntaxCheckerParser.LogicOperatorsContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#logicOperators.
    def exitLogicOperators(self, ctx:PythonSyntaxCheckerParser.LogicOperatorsContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:PythonSyntaxCheckerParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:PythonSyntaxCheckerParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#stat.
    def enterStat(self, ctx:PythonSyntaxCheckerParser.StatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#stat.
    def exitStat(self, ctx:PythonSyntaxCheckerParser.StatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#assignStat.
    def enterAssignStat(self, ctx:PythonSyntaxCheckerParser.AssignStatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#assignStat.
    def exitAssignStat(self, ctx:PythonSyntaxCheckerParser.AssignStatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#exprStat.
    def enterExprStat(self, ctx:PythonSyntaxCheckerParser.ExprStatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#exprStat.
    def exitExprStat(self, ctx:PythonSyntaxCheckerParser.ExprStatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#ifStat.
    def enterIfStat(self, ctx:PythonSyntaxCheckerParser.IfStatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#ifStat.
    def exitIfStat(self, ctx:PythonSyntaxCheckerParser.IfStatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#whileStat.
    def enterWhileStat(self, ctx:PythonSyntaxCheckerParser.WhileStatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#whileStat.
    def exitWhileStat(self, ctx:PythonSyntaxCheckerParser.WhileStatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#forStat.
    def enterForStat(self, ctx:PythonSyntaxCheckerParser.ForStatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#forStat.
    def exitForStat(self, ctx:PythonSyntaxCheckerParser.ForStatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#funcDef.
    def enterFuncDef(self, ctx:PythonSyntaxCheckerParser.FuncDefContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#funcDef.
    def exitFuncDef(self, ctx:PythonSyntaxCheckerParser.FuncDefContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#returnStat.
    def enterReturnStat(self, ctx:PythonSyntaxCheckerParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#returnStat.
    def exitReturnStat(self, ctx:PythonSyntaxCheckerParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#setAssignment.
    def enterSetAssignment(self, ctx:PythonSyntaxCheckerParser.SetAssignmentContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#setAssignment.
    def exitSetAssignment(self, ctx:PythonSyntaxCheckerParser.SetAssignmentContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#operator.
    def enterOperator(self, ctx:PythonSyntaxCheckerParser.OperatorContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#operator.
    def exitOperator(self, ctx:PythonSyntaxCheckerParser.OperatorContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#setLiteral.
    def enterSetLiteral(self, ctx:PythonSyntaxCheckerParser.SetLiteralContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#setLiteral.
    def exitSetLiteral(self, ctx:PythonSyntaxCheckerParser.SetLiteralContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#dictLiteral.
    def enterDictLiteral(self, ctx:PythonSyntaxCheckerParser.DictLiteralContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#dictLiteral.
    def exitDictLiteral(self, ctx:PythonSyntaxCheckerParser.DictLiteralContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#listLiteral.
    def enterListLiteral(self, ctx:PythonSyntaxCheckerParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#listLiteral.
    def exitListLiteral(self, ctx:PythonSyntaxCheckerParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#tupleLiteral.
    def enterTupleLiteral(self, ctx:PythonSyntaxCheckerParser.TupleLiteralContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#tupleLiteral.
    def exitTupleLiteral(self, ctx:PythonSyntaxCheckerParser.TupleLiteralContext):
        pass


    # Enter a parse tree produced by PythonSyntaxCheckerParser#otherStatement.
    def enterOtherStatement(self, ctx:PythonSyntaxCheckerParser.OtherStatementContext):
        pass

    # Exit a parse tree produced by PythonSyntaxCheckerParser#otherStatement.
    def exitOtherStatement(self, ctx:PythonSyntaxCheckerParser.OtherStatementContext):
        pass



del PythonSyntaxCheckerParser