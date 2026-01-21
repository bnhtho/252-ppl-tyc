grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language = Python3;
}
// TODO: Define grammar rules here

program: EOF;

// NOTE: 1.1 Reserved Keywords = Don't declare with these names

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

// NOTE: 1.2 Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHEN: '<';
LESSTHENEQUAL: '<=';
GREATERTHEN: '>';
GREATERTHENEQUAL: '>=';
// NOTE: 1.3 Logical
AND: '&&';
NOT: '!';
OR: '||';
//  NOTE: 1.4 Icrement/Decrement
INCREMENT: '++';
DECREMENT: '--';
// NOTE: 1.5 Assigment
ASSIGMENT: '=';
ACESS: '.'; // NOTE: Member access
// NOTE: 1.6 Seperator
LSB: '[';
RSB: ']';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SEMI: ';';
COMMA: ',';
// Fragments
fragment INTDIGIT: [0-9]+;
fragment ESC_SEQ: '\\' [btnfr"\\];
// intflit
INTLIT: '-'? INTDIGIT;

FLOATLIT:
	// match: 1.23e4, 5.67E-2
	INTDIGIT '.' INTDIGIT ([eE] [+-]? INTDIGIT)?
	| '-'? INTDIGIT [eE] [+-]? INTDIGIT;

STRINGLIT: '"' ( ~["\\] | ESC_SEQ)* '"';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs
// ----------- Stop Here ----------
ERROR_CHAR: .;
ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;
