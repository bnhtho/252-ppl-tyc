# Generated from /home/thohnb/projects/252/252-ppl-tyc/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,5,0,0,
        1,3,1,1,0,0,0,0
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'continue'", 
                     "'default'", "'else'", "'float'", "'for'", "'if'", 
                     "'int'", "'return'", "'string'", "'struct'", "'switch'", 
                     "'void'", "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
                     "'!'", "'||'", "'++'", "'--'", "'='", "'.'", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", 
                      "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESSTHEN", 
                      "LESSTHENEQUAL", "GREATERTHEN", "GREATERTHENEQUAL", 
                      "AND", "NOT", "OR", "INCREMENT", "DECREMENT", "ASSIGMENT", 
                      "ACESS", "LSB", "RSB", "LB", "RB", "LP", "RP", "SEMI", 
                      "COMMA", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CONTINUE=4
    DEFAULT=5
    ELSE=6
    FLOAT=7
    FOR=8
    IF=9
    INT=10
    RETURN=11
    STRING=12
    STRUCT=13
    SWITCH=14
    VOID=15
    WHILE=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    MOD=21
    EQUAL=22
    NOTEQUAL=23
    LESSTHEN=24
    LESSTHENEQUAL=25
    GREATERTHEN=26
    GREATERTHENEQUAL=27
    AND=28
    NOT=29
    OR=30
    INCREMENT=31
    DECREMENT=32
    ASSIGMENT=33
    ACESS=34
    LSB=35
    RSB=36
    LB=37
    RB=38
    LP=39
    RP=40
    SEMI=41
    COMMA=42
    INTLIT=43
    FLOATLIT=44
    STRINGLIT=45
    WS=46
    ERROR_CHAR=47
    ILLEGAL_ESCAPE=48
    UNCLOSE_STRING=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





