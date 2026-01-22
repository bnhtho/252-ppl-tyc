grammar TyC;

options {
	language = Python3;
}

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    return result
}

// ===================== Parser Rules =====================

program: EOF;

// ===================== Keywords =====================

AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// ===================== Operators =====================

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQUAL: '==';
NOTEQUAL: '!=';
LESS_THAN: '<';
LESS_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';

AND: '&&';
OR: '||';
NOT: '!';

INCREMENT: '++';
DECREMENT: '--';

ASSIGNMENT: '=';
ACCESS: '.';

// ===================== Separators =====================

LSB: '[';
RSB: ']';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SEMI: ';';
COMMA: ',';

// ===================== Literals =====================

INTLIT: DIGIT+;

FLOATLIT: DIGIT+ '.' DIGIT* EXP? | '.' DIGIT+ EXP? | DIGIT+ EXP;

STRINGLIT: '"' ( ~["\\\r\n] | ESC_SEQ)* '"';

// ===================== Identifiers =====================

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

// ===================== Fragments =====================

fragment DIGIT: [0-9];
fragment EXP: [eE] [+-]? DIGIT+;
fragment ESC_SEQ: '\\' [btnfr"\\];

// ===================== Whitespace & Comments =====================

WS: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// ===================== Error Handling =====================

ILLEGAL_ESCAPE: '"' ( ~["\\\r\n] | ESC_SEQ)* '\\' .+? '"';

UNCLOSE_STRING: '"' ( ~["\\\r\n] | ESC_SEQ)* ( '\\' . | EOF);

ERROR_CHAR: .;
