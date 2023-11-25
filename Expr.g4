grammar Expr;


prog: (statement|expr)* EOF;



// Expressions
expr:  '(' expr ')'                        #parenExpr
    | left=expr op='^' right=expr        #infixExpr
    | left=expr op=('*'|'/'|'//'|'%') right=expr    #infixExpr
    | left=expr op=('+'|'-') right=expr    #infixExpr
    | left=expr 'and' right=expr           #andExpr
    | left=expr 'or' right=expr            #orExpr
    | 'not' expr                           #notExpr
    | INT                                  #numberExpr
    | FLOAT                                #numberExpr
    | BOOL                                 #boolExpr
    | ID                                   #variableExpr
    | STRING                               #stringExpr
    | func                                  #functionCallExpr
    | list                                  #listExpr
    | index                                  #indexExpr
    |LINE_COMMENT                        #commentExpr
    |BLOCK_COMMENT                     #commentExpr
    ;

assignmentStmt: ID '=' expr;
ifStmt: IF expr ':' statement+ (ELSE ':' statement+)?;
whileStmt: WHILE expr ':' statement+;
forStmt: FOR ID IN expr ':' statement+;
funcDefStmt: DEF ID '(' paramList? ')' (':' returnType)? ':' statement+;
printStmt: PRINT expr;
breakStmt: BREAK;
continueStmt: CONTINUE;
returnStmt: RETURN expr?;


// Expressions


func: ID '(' argList? ')';
argList: expr (',' expr)*;
list: '[' expr? (',' expr)* ']';
index: ID '[' expr ']';

// Parameters and Return Types
paramList: ID (',' ID)*;
returnType: ID;

// Lexer Rules

// Data Types
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+;
STRING: '"' .*? '"';
BOOL: 'True' | 'False';

// Operators
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_MOD: '%';
OP_FLOOR_DIV: '//';
OP_POW: '^';

// Keywords
PRINT: 'print';
FOR: 'for';
BREAK: 'break';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
IN: 'in';
DEF: 'def';
RETURN: 'return';
CONTINUE: 'continue';

// Whitespace and Comments
WS: [ \t\r\n] -> skip;
LINE_COMMENT: '#' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Relational Operators
GREATER_THAN: '>';
LESS_THAN: '<';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
EQUAL: '==';
NOT_EQUAL: '!=';

// Statements
statement: assignmentStmt
         | ifStmt
         | whileStmt
         | funcDefStmt
         | printStmt
         | breakStmt
         | continueStmt
         | returnStmt
         |paramList
         ;


