// Expr.g4

grammar Test;

prog: (statement | functionDeclaration)+ EOF;

statement:
    variableDeclaration
    | assignment
    | ifStatement
    | whileStatement
    | forStatement
    | printStatement
    | returnStatement
    ;

variableDeclaration:
    'var' ID ('=' expression)? ';'
    ;

assignment:
    ID '=' expression ';'
    ;

ifStatement:
    'if' '(' expression ')' block ('else' block)?
    ;

whileStatement:
    'while' '(' expression ')' block
    ;

forStatement:
    'for' '(' variableDeclaration? ';' expression? ';' assignment? ')' block
    ;

printStatement:
    'print' expression ';'
    ;

returnStatement:
    'return' expression? ';'
    ;

block:
    '{' statement* '}'
    ;

expression:
    orExpression
    ;

orExpression:
    andExpression ('or' andExpression)*
    ;

andExpression:
    compExpression ('and' compExpression)*
    ;

compExpression:
    addExpression (('<' | '>' | '<=' | '>=' | '==' | '!=') addExpression)*
    ;

addExpression:
    multExpression (('+' | '-') multExpression)*
    ;

multExpression:
    unaryExpression (('*' | '/' | '%' | '//') unaryExpression)*
    ;

unaryExpression:
    '-' unaryExpression
    | primaryExpression
    ;

primaryExpression:
    '(' expression ')'
    | literal
    | ID
    | functionCall
    ;

literal:
    INT
    | FLOAT
    | BOOL
    | STRING
    | NONE
    ;

functionDeclaration:
    'def' ID '(' parameterList? ')' block
    ;

parameterList:
    ID (',' ID)*
    ;

functionCall:
    ID '(' argumentList? ')'
    ;

argumentList:
    expression (',' expression)*
    ;

// Define tokens for literals
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?;
BOOL: 'True' | 'False';
STRING: '"' .*? '"';
NONE: 'None';

// Define an identifier token
ID: [a-zA-Z_][a-zA-Z_0-9]*;

// Skip whitespace and newline characters
WS: [ \t\r\n]+ -> skip;
