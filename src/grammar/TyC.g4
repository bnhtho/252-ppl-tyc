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
// Step 1: Grammar Rules

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs
// ----------- Stop Here ----------
ERROR_CHAR: .;
ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;
