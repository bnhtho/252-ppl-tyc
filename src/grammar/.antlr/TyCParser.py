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
        4,1,52,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,56,8,1,10,1,12,1,59,9,
        1,1,2,1,2,1,3,1,3,1,3,1,3,3,3,67,8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        75,8,3,1,3,3,3,78,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,90,8,4,1,4,0,1,2,5,0,2,4,6,8,0,1,5,0,7,7,10,10,12,12,15,15,46,
        46,103,0,10,1,0,0,0,2,12,1,0,0,0,4,60,1,0,0,0,6,77,1,0,0,0,8,89,
        1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,6,1,-1,0,13,14,5,30,0,0,
        14,15,3,2,1,1,15,57,1,0,0,0,16,17,10,14,0,0,17,18,5,17,0,0,18,56,
        3,2,1,15,19,20,10,13,0,0,20,21,5,18,0,0,21,56,3,2,1,14,22,23,10,
        12,0,0,23,24,5,19,0,0,24,56,3,2,1,13,25,26,10,11,0,0,26,27,5,20,
        0,0,27,56,3,2,1,12,28,29,10,10,0,0,29,30,5,21,0,0,30,56,3,2,1,11,
        31,32,10,9,0,0,32,33,5,22,0,0,33,56,3,2,1,10,34,35,10,8,0,0,35,36,
        5,23,0,0,36,56,3,2,1,9,37,38,10,7,0,0,38,39,5,24,0,0,39,56,3,2,1,
        8,40,41,10,6,0,0,41,42,5,25,0,0,42,56,3,2,1,7,43,44,10,5,0,0,44,
        45,5,26,0,0,45,56,3,2,1,6,46,47,10,4,0,0,47,48,5,27,0,0,48,56,3,
        2,1,5,49,50,10,3,0,0,50,51,5,28,0,0,51,56,3,2,1,4,52,53,10,2,0,0,
        53,54,5,29,0,0,54,56,3,2,1,3,55,16,1,0,0,0,55,19,1,0,0,0,55,22,1,
        0,0,0,55,25,1,0,0,0,55,28,1,0,0,0,55,31,1,0,0,0,55,34,1,0,0,0,55,
        37,1,0,0,0,55,40,1,0,0,0,55,43,1,0,0,0,55,46,1,0,0,0,55,49,1,0,0,
        0,55,52,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,3,1,
        0,0,0,59,57,1,0,0,0,60,61,7,0,0,0,61,5,1,0,0,0,62,63,3,4,2,0,63,
        66,5,46,0,0,64,65,5,33,0,0,65,67,3,2,1,0,66,64,1,0,0,0,66,67,1,0,
        0,0,67,68,1,0,0,0,68,69,5,41,0,0,69,78,1,0,0,0,70,71,5,1,0,0,71,
        74,5,46,0,0,72,73,5,33,0,0,73,75,3,2,1,0,74,72,1,0,0,0,74,75,1,0,
        0,0,75,76,1,0,0,0,76,78,5,41,0,0,77,62,1,0,0,0,77,70,1,0,0,0,78,
        7,1,0,0,0,79,80,3,4,2,0,80,81,5,46,0,0,81,82,5,41,0,0,82,90,1,0,
        0,0,83,84,3,4,2,0,84,85,5,46,0,0,85,86,5,33,0,0,86,87,3,2,1,0,87,
        88,5,41,0,0,88,90,1,0,0,0,89,79,1,0,0,0,89,83,1,0,0,0,90,9,1,0,0,
        0,6,55,57,66,74,77,89
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
                     "'||'", "'!'", "'++'", "'--'", "'='", "'.'", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", 
                      "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESS_THAN", 
                      "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "AND", 
                      "OR", "NOT", "INCREMENT", "DECREMENT", "ASSIGNMENT", 
                      "ACCESS", "LSB", "RSB", "LB", "RB", "LP", "RP", "SEMI", 
                      "COMMA", "INTLIT", "FLOATLIT", "STRINGLIT", "IDENTIFIER", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_type = 2
    RULE_varDecl = 3
    RULE_strucDecl = 4

    ruleNames =  [ "program", "expr", "type", "varDecl", "strucDecl" ]

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
    LESS_THAN=24
    LESS_EQUAL=25
    GREATER_THAN=26
    GREATER_EQUAL=27
    AND=28
    OR=29
    NOT=30
    INCREMENT=31
    DECREMENT=32
    ASSIGNMENT=33
    ACCESS=34
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
    IDENTIFIER=46
    WS=47
    LINE_COMMENT=48
    BLOCK_COMMENT=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    ERROR_CHAR=52

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
            self.state = 10
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def MUL(self):
            return self.getToken(TyCParser.MUL, 0)

        def DIV(self):
            return self.getToken(TyCParser.DIV, 0)

        def MOD(self):
            return self.getToken(TyCParser.MOD, 0)

        def EQUAL(self):
            return self.getToken(TyCParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(TyCParser.NOTEQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(TyCParser.LESS_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(TyCParser.LESS_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(TyCParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(TyCParser.GREATER_EQUAL, 0)

        def AND(self):
            return self.getToken(TyCParser.AND, 0)

        def OR(self):
            return self.getToken(TyCParser.OR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(TyCParser.NOT)
            self.state = 14
            self.expr(1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 17
                        self.match(TyCParser.ADD)
                        self.state = 18
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 20
                        self.match(TyCParser.SUB)
                        self.state = 21
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 23
                        self.match(TyCParser.MUL)
                        self.state = 24
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 26
                        self.match(TyCParser.DIV)
                        self.state = 27
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 29
                        self.match(TyCParser.MOD)
                        self.state = 30
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 32
                        self.match(TyCParser.EQUAL)
                        self.state = 33
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 35
                        self.match(TyCParser.NOTEQUAL)
                        self.state = 36
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 38
                        self.match(TyCParser.LESS_THAN)
                        self.state = 39
                        self.expr(8)
                        pass

                    elif la_ == 9:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 41
                        self.match(TyCParser.LESS_EQUAL)
                        self.state = 42
                        self.expr(7)
                        pass

                    elif la_ == 10:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 44
                        self.match(TyCParser.GREATER_THAN)
                        self.state = 45
                        self.expr(6)
                        pass

                    elif la_ == 11:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 47
                        self.match(TyCParser.GREATER_EQUAL)
                        self.state = 48
                        self.expr(5)
                        pass

                    elif la_ == 12:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        self.match(TyCParser.AND)
                        self.state = 51
                        self.expr(4)
                        pass

                    elif la_ == 13:
                        localctx = TyCParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 53
                        self.match(TyCParser.OR)
                        self.state = 54
                        self.expr(3)
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744215680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_varDecl




    def varDecl(self):

        localctx = TyCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 10, 12, 15, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.type_()
                self.state = 63
                self.match(TyCParser.IDENTIFIER)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 64
                    self.match(TyCParser.ASSIGNMENT)
                    self.state = 65
                    self.expr(0)


                self.state = 68
                self.match(TyCParser.SEMI)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(TyCParser.AUTO)
                self.state = 71
                self.match(TyCParser.IDENTIFIER)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 72
                    self.match(TyCParser.ASSIGNMENT)
                    self.state = 73
                    self.expr(0)


                self.state = 76
                self.match(TyCParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrucDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_strucDecl




    def strucDecl(self):

        localctx = TyCParser.StrucDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_strucDecl)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.type_()
                self.state = 80
                self.match(TyCParser.IDENTIFIER)
                self.state = 81
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.type_()
                self.state = 84
                self.match(TyCParser.IDENTIFIER)
                self.state = 85
                self.match(TyCParser.ASSIGNMENT)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




