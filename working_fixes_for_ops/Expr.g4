grammar Expr;
 
prog: expr EOF;
 
expr
    : left=expr op=('+'|'-') right=multExpr   #addSubExpr
    | multExpr                                #multExprPass
    ;

multExpr
    : left=multExpr op=('*'|'/') right=powExpr  #multDivExpr
    | powExpr                                    #powExprPass
    ;

powExpr
    : unaryExpr (op='**' powExpr)?  #rightAssociativePowExpr
    ;

unaryExpr
    : data_structures                #dataTypeExpr
    | '(' expr ')'                   #parensExpr
    ;

data_structures
    : int                            
    | float                          
    | bool                          
    | string                         
    | tuple                         
    | list                           
    | dict                           
    | ID                             
    | none                          
    | set                            
    ;

int: INT| 'INT';
float: FLOAT| 'FLOAT';
bool: BOOL| 'BOOL';
string: STRING| 'STRING';
tuple: TUPLE| 'TUPLE';

none: NONE| 'NONE';




dict
    :   '{' (data_structures ':' expr (',' data_structures ':' expr)*)? '}'
    |   'DICT'
    ;

set
    :   '{' expr (',' expr)* '}'
    |   'SET'
    ;

list
    :   '[' (expr (',' expr)* | expr for_expr+ )* ']'
    |   'LIST'
    ;
for_expr
    :   'for' ID 'in' expr ( if_expr )?
    ;

if_expr
    :   'if' expr ( 'else' expr )?
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_POW: '**';
 
NEWLINE : [\r\n]+ ;
INT     : [0-9]+;
FLOAT   : [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ;
BOOL    : 'True' | 'False' ;
STRING  : '"' .*? '"';
TUPLE   : '(' .*? ')';
NONE    : 'None';
ID      : [a-zA-Z_][a-zA-Z_0-9]*;
WS      : [ \t]+ -> skip;
