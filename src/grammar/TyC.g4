grammar TyC;

options {
	language = Python3;
}

/* ======================= LEXER SETUP =======================
 */

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

/* ======================= PARSER ROOT =======================
 */

program: decl* EOF;
decl: structDecl | funcDecl;

/* ======================= KEYWORDS =======================
 */

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

/* ======================= OPERATORS =======================
 */

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

/* ======================= SEPARATORS =======================
 */

LSB: '[';
RSB: ']';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';

/* ======================= LITERALS =======================
 */

INTLIT: DIGIT+;

FLOATLIT: DIGIT+ '.' DIGIT* EXP? | '.' DIGIT+ EXP? | DIGIT+ EXP;

STRINGLIT:
	'"' (~["\\\r\n] | ESC_SEQ)* '"' { self.text = self.text[1:-1] };

/* ======================= IDENTIFIERS =======================
 */

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

/* ======================= FRAGMENTS =======================
 */

fragment DIGIT: [0-9];
fragment EXP: [eE] [+-]? DIGIT+;
fragment ESC_SEQ: '\\' [btnfr"\\];

/* ======================= WHITESPACE & COMMENTS =======================
 */

WS: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

// BLOCK_COMMENT: '/*' .*? '*/' -> skip;
BLOCK_COMMENT: '/*' .*? ('*/' | EOF) -> skip;
/* ======================= LEXER ERRORS =======================
 */

// ERROR
UNCLOSE_STRING:
	'"' (ESC_SEQ | ~["\\\r\n])* '\n' {
            self.text = self.text[1:]
        }
	| '"' (ESC_SEQ | ~["\\\r\n])* '\r\n' {
            self.text = self.text[1:]
        }
	| '"' (ESC_SEQ | ~["\\\r\n])* EOF {
            self.text = self.text[1:]
        };
ILLEGAL_ESCAPE:
	'"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[btnrf"\\] { self.text = self.text[1:]; };
ERROR_CHAR: .;

/* ======================= EXPRESSIONS =======================
 */

expr: assignExpr;

/* Assignment (right associative) */
assignExpr: logicalOrExpr (ASSIGNMENT assignExpr)?;

/* Logical OR / AND */
logicalOrExpr: logicalAndExpr (OR logicalAndExpr)*;

logicalAndExpr: equalityExpr (AND equalityExpr)*;

/* Equality & relational */
equalityExpr:
	relationalExpr ((EQUAL | NOTEQUAL) relationalExpr)*;

relationalExpr:
	additiveExpr (
		(LESS_THAN | LESS_EQUAL | GREATER_THAN | GREATER_EQUAL) additiveExpr
	)*;

/* Arithmetic */
additiveExpr:
	multiplicativeExpr ((ADD | SUB) multiplicativeExpr)*;

multiplicativeExpr: unaryExpr ((MUL | DIV | MOD) unaryExpr)*;

/* Unary */
unaryExpr: (NOT | ADD | SUB | INCREMENT | DECREMENT) unaryExpr
	| postfixExpr;

/* Postfix */
postfixExpr: primaryExpr postfixPart*;

postfixPart: postfixOp | LP argList? RP;

postfixOp: INCREMENT | DECREMENT | ACCESS IDENTIFIER;

/* Primary */
primaryExpr:
	IDENTIFIER
	| INTLIT
	| FLOATLIT
	| STRINGLIT
	| LP expr RP
	| structLiteral;

/* ======================= LITERALS & TYPES =======================
 */

structLiteral: LB expr (COMMA expr)* RB;

argList: expr (COMMA expr)*;

builtinType: INT | FLOAT | STRING | VOID;

type: builtinType | IDENTIFIER;

/* ======================= DECLARATIONS =======================
 */

varDecl:
	type IDENTIFIER (ASSIGNMENT expr)? SEMI
	| AUTO IDENTIFIER (ASSIGNMENT expr)? SEMI;
structMember: type IDENTIFIER SEMI;

structDecl: STRUCT IDENTIFIER LB structMember* RB SEMI;

/* ======================= STATEMENTS =======================
 */

stmt:
	exprstmt
	| varDecl
	| blockstmt
	| ifstmt
	| forstmt
	| whilestmt
	| breaksmt
	| continuestmt
	| switchstmt
	| returnstmt;

blockstmt: LB stmt* RB;

ifstmt: IF LP expr RP stmt (ELSE stmt)?;

whilestmt: WHILE LP expr RP stmt;

breaksmt: BREAK SEMI;

continuestmt: CONTINUE SEMI;

returnstmt: RETURN expr? SEMI;

/* ======================= FOR LOOP =======================
 */

forstmt: FOR LP forInit? SEMI expr? SEMI expr? RP stmt;

forInit: varDeclFor | expr;

varDeclFor: (builtinType | AUTO) IDENTIFIER (ASSIGNMENT expr)?;

/* ======================= SWITCH =======================
 */

switchstmt: SWITCH LP expr RP LB caseBlock* defaultBlock? RB;

caseBlock: CASE (ADD | SUB)? INTLIT COLON stmt*;

defaultBlock: DEFAULT COLON stmt*;

/* ======================= FUNCTIONS =======================
 */

funcDecl:
	type IDENTIFIER LP paramList? RP blockstmt
	| IDENTIFIER LP paramList? RP blockstmt;

paramList: param (COMMA param)*;

param: type IDENTIFIER;

/* ======================= EXPRESSION STATEMENT =======================
 */

exprstmt: expr SEMI;
