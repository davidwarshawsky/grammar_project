grammar PythonSyntaxChecker;
/*
This file is for checking python syntax checking and we return true or false based on if there are any issues. The first issue detected is raised.
This is run before compiling the code.
*/

prog: expr EOF;

expr: left=expr op='^'       right=expr   #infixExpr
    | left=expr op=('+'|'-') right=expr   #infixExpr
    | left=expr op=('*'|'/') right=expr   #infixExpr
    | left=expr op=('&'|'|'|'~'|'<<'|'>>') right=expr   #infixExpr
    | '(' expr ')'                        #parenExpr
    | ID                                  #variableExpr
    |number                               #numberExpr
    |lambda                               #lambdaExpr
    |def                                  #defExpr
    |funcCall                             #funcCallExpr
    ;


number: INT | FLOAT;
lambda: 'lambda' ID ':' expr;
def: ID '(' paramList? '):' '{' stat* '}';

paramList: ID (',' ID)*;

// Lexer Rules
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_MOD: '%';
OP_EXP: '**';
OP_XOR: '^';
OP_FLOOR_DIV: '//';

BITWISE_AND: '&';        // Bitwise AND
BITWISE_OR: '|';         // Bitwise OR
BITWISE_NOT: '~';        // Bitwise NOT
BITWISE_SHIFT_LEFT: '<<';  // Bitwise Shift Left
BITWISE_SHIFT_RIGHT: '>>'; // Bitwise Shift Right


funcCall: ID '(' argList? ')';

argList: expr (',' expr)*;

statement: setAssignment | otherStatement;
//
literal: INT | FLOAT | STRING | BOOL | listLiteral | tupleLiteral | dictLiteral | setLiteral;
assignmentOperator: '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '^=' | '**=' | '//=';
membershipOperator: 'in' | 'not in';
identityOperator: 'is' | 'is not';
logicOperators: 'and' | 'or' | 'not';
comparisonOperator: '==' | '!=' | '<' | '>' | '<=' | '>=';

//Statements in Python
stat:assignStat
    | exprStat
    | ifStat
    | whileStat
    | forStat
    | funcDef
    | returnStat
    | 'break' ';'
    | 'continue' ';'
    | 'pass' ';'
    | 'print' exprStat
    ;


assignStat: ID assignmentOperator expr ';';

exprStat: expr ';';

ifStat: 'if' expr ':' stat+ ('elif' expr ':' stat+)* ('else' ':' stat+)?;

whileStat: 'while' expr ':' stat+;

forStat: 'for' ID 'in' expr ':' stat+;

funcDef: 'def' ID '(' paramList? '):' '{' stat* '}';

returnStat: 'return' expr ';';


setAssignment: ID '=' literal ';';

operator: assignmentOperator  | membershipOperator | identityOperator | logicOperators | comparisonOperator;


setLiteral: '{' (expr (',' expr)*)? '}';
dictLiteral: '{' (expr ':' expr (',' expr ':' expr)*)? '}';
listLiteral: '[' (expr (',' expr)*)? ']';
tupleLiteral: '(' (expr (',' expr)*)? ')';

otherStatement: ifStat | forStat | whileStat;

// Lexer Rules
ID: [a-zA-Z_][a-zA-Z_0-9]*;
BOOL: 'True' | 'False';
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+;
STRING: '"' .*? '"';

// Whitespace and comments
WS: [ \t\r\n] -> channel(HIDDEN);
NEWLINE: [\r\n]+ ;
INDENT: [ \t]+ -> channel(HIDDEN);

COMMENT: '#' ~[\r\n]* -> channel(HIDDEN);
MULTILINE_COMMENT: '"""' .*? '"""' -> channel(HIDDEN);