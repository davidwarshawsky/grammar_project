grammar PythonSyntaxChecker;
/*
This file is for checking python syntax checking and we return true or false based on if there are any issues. The first issue detected is raised.
This is run before compiling the code.
*/



prog: expr EOF;

/* We want to define all expressions that exist in python. Let's look up a list.
*/
expr
// Data structures.
    : 
    | INT
    | STRING
    | DICT
    | LIST
    | TUPLE
    | SET
    | NONE
    | BOOL
    | FLOAT
    | COMMENTLINE
    | NEWLINE
    | left=operation_data_structure op=operation       right=operation_data_structure   #infixExpr
    | ID
    ;
// | ID # variableExpr
// | INT                                 #numberExpr
// | '(' expr ')'                        #parensExpr
operation_data_structure: ID
    | INT
    | STRING
    | DICT
    | LIST
    | TUPLE
    | SET
    | NONE
    | BOOL
    | FLOAT
    ;
operation: expr (op=('*'|'/'|'+'|'-') expr)*;


def : ID '(' ID (',' ID)* '):' '{' stat* '}' ;

//Lexer Rules
/* Arithmetic Operators */
/*
Add/Subtract operations allow:
- int + int
- float + float
- int + float
- float + int
- string + string
- list + list
- tuple + tuple
- set + set
- dict + dict
- dict + list
- list + tuple
- tuple + list
 */
OP_ADD: '+';
/*
Subtraction operations allow:
- int - int
- float - float
- int - float
- float - int
 */
OP_SUB: '-';
/*
Multiplication operations allow:
- int * int
- float * float
- int * float
- float * int
- string * int
- int * string
- list * int
- int * list
- tuple * int
- int * tuple
- int * bool
- bool * int
*/
OP_MUL: '*';
/*
Division operations allow:
- int / int
- float / float
- int / float
- float / int
*/
OP_DIV: '/';
/*
Modulo operations allow:
- int % int
- float % float
- int % float
- float % int
*/
OP_MOD: '%';
/*
Exponent operations allow:
- int ** int
- float ** float
- int ** float
- float ** int
*/
OP_EXP: '**';
/*
XOR operations allow:
- int ^ int
- float ^ float
- int ^ float
- float ^ int
*/
OP_XOR: '^';
/*
Floor Division operations allow:
- int // int
- float // float
- int // float
- float // int
*/
OP_FLOOR_DIV: '//';

ops
    : OP_ADD
    | OP_SUB
    | OP_MUL
    | OP_DIV
    | OP_MOD
    | OP_EXP
    | OP_XOR
    | OP_FLOOR_DIV
    ;


// create an assignment operator for a python variable in antlr4
assignmentOperator: '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '^=' | '**=' | '//=';

assignment: ID assignmentOperator expr ';';

expr: ID | INT | STRING | '(' expr ')' | expr '+' expr | expr '-' expr | expr '*' expr | expr '/' expr;

funcCall: ID '(' expr (',' expr)* ')';

FOR: 'for';
IN: 'in';
COLON: ':';
WHILE: 'while';

BREAK: 'break';
CONTINUE: 'continue';

iterable_expr
            : ID
            | INT
            | STRING
            | DICT
            | LIST
            | TUPLE
            | SET;

boolean_expr
            : iterable_expr
            | BOOL
            | FLOAT
            | NONE
            | funcCall
            | for_loop_declaration
            | while_loop_declaration
            | if_else_elif_statement
            | BREAK
            | CONTINUE
            ;

for_loop_declaration: FOR ID IN iterable_expr COLON;
while_loop_declaration: WHILE expr COLON;

IF: 'if';
ELIF: 'elif';
ELSE: 'else';
if_else_elif_statement
                        : IF expr COLON
                        (ELIF expr COLON)*
                        (ELSE COLON)?
                        ;




stat: ID '=' expr ';'
    | expr ';'
    ;

bitwiseOperator : '&' | '|' | '^'| '~'| '<<' | ' >>' ;

membershipOperator: 'in' | 'not in';
identityOperator: 'is' | 'is not';
logicOperators: 'and' | 'or' | 'not';
comparisonOperator: '==' | '!=' | '<' | '>' | '<=' | '>=';


// Data Types:
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
BOOL: 'True' | 'False' ;
INT     : [0-9]+ ;


// Trying to do bitwise operations on FLOAT converts it to INT first so it's ok to use bitwise operations on them.
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ;


// Bitwise Operations are not defined for the below Data Types.
STRING: '"' .*? '"';
DICT: '{' .*? '}';
LIST: '[' .*? ']';
TUPLE: '(' .*? ')';
SET: '{' .*? '}';
NONE: 'None' ;

// Symbols:
WS: [ \t]+ -> skip;
NEWLINE : [\r\n]+ ;
INDENT : [\s\t]+ ;
ANY: ~[\r\n]*;


COMMENTLINE: ANY '#' + ANY;

