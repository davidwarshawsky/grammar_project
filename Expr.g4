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
    | ID '=' expr                   #assignmentExpression
    | if_statement_expr             #ifStatementExpression
    | for_loop_expr                 #forLoopExpression
    | while_loop_expr               #whileLoopExpression
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
if_statement_expr
    :   'if' expr ':' expr ( 'elif' expr ':' expr )* ( 'else' ':' expr )?
    ;

for_loop_expr
    :   'for' ID 'in' expr ':' #for_loop_expression
    ;
while_loop_expr
    :   'while' expr ':' #while_loop_expression
    ;


OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_POW: '**';

// NEWLINE : [\r\n]+ ;

// NEW_STRING: '"' (~['\\', '\n', '"'] | '\\' ~[\n])* '"';
// NEW_1STRING: '"' ('""' | '''' ~['\n', '"'] | '\\' ~[\n])* '"';

// strings: opening = QUOTE (~[\'\""]*? | '""' | '\'\'')* '\\\n)'? closing = QUOTE;
QUOTE: ('"' | '\'');
stringz: opening = QUOTE (~['"]*? | '""' | '\'\'')* '\\\n'? closing = QUOTE;


INT     : [0-9]+;
FLOAT   : [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ;
BOOL    : 'True' | 'False';
STRING  : '"' .*? '"';
WS      : [ \t\n]+ -> skip;

NONE    : 'None';
ID      : [a-zA-Z_][a-zA-Z_0-9]*;