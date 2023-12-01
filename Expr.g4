grammar Expr;
 
prog: expr EOF;




expr
    : left=expr op='or' right=andExpr  #orExpression
    | andExpr  #andExprPass
    ;

andExpr
    : left=andExpr op='and' right=compExpr  #andExpression
    | compExpr  #compExprPass
    ;

compExpr
    : left=compExpr op=('<' | '>' | '<=' | '>=' | '==' | '!=') right=bitOrExpr  #compExpression
    | bitOrExpr  #bitOrExprPass
    ;

bitOrExpr
    : left=bitOrExpr op='|' right=bitXorExpr  #bitOrExpression
    | bitXorExpr  #bitXorExprPass
    ;

bitXorExpr
    : left=bitXorExpr op='^' right=bitAndExpr  #bitXorExpression
    | bitAndExpr  #bitAndExprPass
    ;

bitAndExpr
    : left=bitAndExpr op='&' right=bitShiftExpr  #bitAndExpression
    | bitShiftExpr  #bitShiftExprPass
    ;

bitShiftExpr
    : left=bitShiftExpr op=('<<' | '>>') right=addExpr  #bitShiftExpression
    | addExpr  #addExprPass
    ;

addExpr
    : left=addExpr op=('+'|'-') right=multExpr   #addSubExpression
    | multExpr  #multExprPass
    ;


multExpr
    : left=multExpr op=('*' | '/' | '%' | '//') right=powExpr  #multDivExpression
    | powExpr                                    #powExprPass
    ;

powExpr
    : unaryExpr (op='**' powExpr)?  #rightAssociativePowExpression
    ;

unaryExpr
    : '(' expr ')'                   #parensExpression
    | data_structures                #dataTypeExpression
    ;

data_structures
    : int                            
    | float                          
    | bool                          
    | string                         
    | tuple                         
    | list                           
    | dict                           
    | none                          
    | set            
    | ID                             
    ;

int: INT| 'INT';
float: FLOAT| 'FLOAT';
bool: BOOL| 'BOOL';
string: STRING| 'STRING';

none: NONE| 'NONE';

tuple
    :   '(' expr ',' expr (',' expr)* ')'
    |   'TUPLE'
    ;


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
NONE    : 'None';
ID      : [a-zA-Z_][a-zA-Z_0-9]*;
WS      : [ \t]+ -> skip;
