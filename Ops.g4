grammar Ops;

prog: expr EOF;

expr
    : data_structures op='**' expr
    | expr op=('*' | '/' | '%' | '//') expr
    | expr op=('+' | '-') expr
    | expr op=('<' | '>' | '<=' | '>=' | '==' | '!=') expr
    | expr op='|' expr
    | expr op='^' expr
    | expr op='&' expr
    | expr op=('<<' | '>>') expr
    | expr op='and' expr
    | expr op='or' expr
    | data_structures;


data_structures
    : INT                   
    | FLOAT                 
    | BOOL                  
    | STRING                
    | TUPLE                 
    | list
    | dict
    | ID
    | NONE
    | set
    ;

dict
    :   '{' (data_structures ':' expr (',' data_structures ':' expr)* | data_structures ':' expr for_expr+ )? '}'
    ;

set
    :   '{' expr (',' expr)* '}'
    ;

list
    :   '[' (expr (',' expr)* | expr for_expr+ )* ']'
    ;
for_expr
    :   'for' ID 'in' expr ( if_expr )?
    ;

if_expr
    :   'if' expr ( 'else' expr )?
    ;




/*Data Types: */
ID: [a-zA-Z_][a-zA-Z_0-9]*;
BOOL: 'True' | 'False' ;
DICT: '{' .*? '}';
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ;
INT     : [0-9]+;
SET: '{' .*? '}';
STRING: '"' .*? '"';
TUPLE: '(' .*? ')';
NONE: 'None';
WS: [ \t]+ -> skip;



/*OPS */
// OP_NOT: '~';
// OP_LOGICAL_NOT: 'not';


// immutable_data_structures
//     : INT                   
//     | FLOAT
//     | BOOL
//     | STRING                
//     | TUPLE                 
//     ;