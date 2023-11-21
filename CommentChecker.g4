
grammar CommentChecker;

file: COMMENTLINE + EOF;

COMMENTLINE: WS '#' + ANY;

WS: [ \t]+ -> skip;
// emptyString: /* empty alternative */;
ANY: ~[\r\n]*;

