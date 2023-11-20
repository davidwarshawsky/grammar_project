grammar PythonSyntaxChecker;
/*
This file is for checking python syntax checking and we return true or false based on if there are any issues. The first issue detected is raised.
This is run before compiling the code.
*/



prog: expr EOF;

/* We want to define all expressions that exist in python. Let's look up a list.
*/
expr: left=expr op='^'       right=expr   #infixExpr
    | left=expr op=('+'|'-') right=expr   #infixExpr
    | left=expr op=('*'|'/') right=expr   #infixExpr
    | INT                                 #numberExpr
    | '(' expr ')'                        #parensExpr
    | ID # variableExpr
    | lambdaExpr                          #lambdaExpr
    ;
def : ID '(' ID (',' ID)* '):' '{' stat* '}' ;
lambdaExpr: 'lambda' ID (',' ID)* ':' expr;
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


// create an assignment operator for a python variable in antlr4
assignmentOperator: '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '^=' | '**=' | '//=';

assignment: ID assignmentOperator expr ';';

expr: ID | INT | STRING | '(' expr ')' | expr '+' expr | expr '-' expr | expr '*' expr | expr '/' expr;

funcCall: ID '(' expr (',' expr)* ')';



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


// Symbols:
WS      : [ \t\r\n] -> channel(HIDDEN);
NEWLINE : [\r\n]+ ;
INDENT : [\s\t]+ ;

//Comment
COMMENT: '#' ~[\r\n]* -> channel(HIDDEN);
MULTILINE_COMMENT : '"""' .*? '"""' -> channel(HIDDEN);

// I'm not sure what to do with otherStatement yet.
statement: setAssignment | otherStatement;

setAssignment: ID '=' setLiteral ';';

setLiteral: '{' (expr (',' expr)*)? '}';

dictLiteral: '{' (expr ':' expr (',' expr ':' expr)*)? '}';

tupleLiteral: '(' (expr (',' expr)*)? ')';

listLiteral: '[' (expr (',' expr)*)? ']';
// Control flow statements
ifStatement: 'if' expr ':' statement+ ('elif' expr ':' statement+)* ('else' ':' statement+)?;
forStatement: 'for' ID 'in' expr ':' statement+;
whileStatement: 'while' expr ':' statement+;
