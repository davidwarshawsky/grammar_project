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
    | SET                   
    | LIST                  
    | DICT              
    ;

/*OPS */
// OP_NOT: '~';
// OP_LOGICAL_NOT: 'not';


/*Data Types: */
BOOL: 'True' | 'False' ;
DICT: '{' .*? '}';
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ;
INT     : [0-9]+;
LIST: '[' .*? ']';
SET: '{' .*? '}';
STRING: '"' .*? '"';
TUPLE: '(' .*? ')';
NONE: 'None';
WS: [ \t]+ -> skip;
