# Generated from Ops.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OpsParser import OpsParser
else:
    from OpsParser import OpsParser

# This class defines a complete generic visitor for a parse tree produced by OpsParser.

class OpsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OpsParser#prog.
    def visitProg(self, ctx:OpsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#expr.
    def visitExpr(self, ctx:OpsParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#data_structures.
    def visitData_structures(self, ctx:OpsParser.Data_structuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#immutable_data_structures.
    def visitImmutable_data_structures(self, ctx:OpsParser.Immutable_data_structuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#dict.
    def visitDict(self, ctx:OpsParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#set.
    def visitSet(self, ctx:OpsParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#list.
    def visitList(self, ctx:OpsParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#for_expr.
    def visitFor_expr(self, ctx:OpsParser.For_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpsParser#if_expr.
    def visitIf_expr(self, ctx:OpsParser.If_exprContext):
        return self.visitChildren(ctx)



del OpsParser