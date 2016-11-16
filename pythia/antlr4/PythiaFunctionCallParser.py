# Generated from /Users/enrique/workspace/other/frontline/pythia/PythiaFunctionCall.g4 by ANTLR 4.5.3
# encoding: utf-8
from io import StringIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\t")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\7\5 \n\5\f\5\16\5#\13\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5)\n\5\3\6\3\6\3\6\3\6\5\6/\n\6\3\6\2\2\7\2\4")
        buf.write("\6\b\n\2\2\61\2\f\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2\b")
        buf.write("(\3\2\2\2\n.\3\2\2\2\f\r\7\3\2\2\r\22\5\4\3\2\16\17\7")
        buf.write("\4\2\2\17\21\5\6\4\2\20\16\3\2\2\2\21\24\3\2\2\2\22\20")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\22\3\2\2\2\25")
        buf.write("\26\7\5\2\2\26\3\3\2\2\2\27\30\7\6\2\2\30\5\3\2\2\2\31")
        buf.write("\32\5\n\6\2\32\7\3\2\2\2\33\34\7\3\2\2\34!\5\n\6\2\35")
        buf.write("\36\7\4\2\2\36 \5\n\6\2\37\35\3\2\2\2 #\3\2\2\2!\37\3")
        buf.write("\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$%\7\5\2\2%)\3\2")
        buf.write("\2\2&\'\7\3\2\2\')\7\5\2\2(\33\3\2\2\2(&\3\2\2\2)\t\3")
        buf.write("\2\2\2*/\5\b\5\2+/\7\6\2\2,/\7\7\2\2-/\7\b\2\2.*\3\2\2")
        buf.write("\2.+\3\2\2\2.,\3\2\2\2.-\3\2\2\2/\13\3\2\2\2\6\22!(.")
        return buf.getvalue()


class PythiaFunctionCallParser(Parser):
    grammarFileName = "PythiaFunctionCall.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'['", "','", "']'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "STRING", "INTEGER", "FLOAT", "WS"]

    RULE_call = 0
    RULE_full_function_name = 1
    RULE_argument = 2
    RULE_array = 3
    RULE_value = 4

    ruleNames = ["call", "full_function_name", "argument", "array", "value"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    STRING = 4
    INTEGER = 5
    FLOAT = 6
    WS = 7

    def __init__(self, input: TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA,
                                          self.sharedContextCache)
        self._predicates = None

    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def full_function_name(self):
            return self.getTypedRuleContext(
                PythiaFunctionCallParser.Full_function_nameContext, 0)

        def argument(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    PythiaFunctionCallParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(
                    PythiaFunctionCallParser.ArgumentContext, i)

        def getRuleIndex(self):
            return PythiaFunctionCallParser.RULE_call

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCall"):
                listener.enterCall(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCall"):
                listener.exitCall(self)

    def call(self):

        localctx = PythiaFunctionCallParser.CallContext(self, self._ctx,
                                                        self.state)
        self.enterRule(localctx, 0, self.RULE_call)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(PythiaFunctionCallParser.T__0)
            self.state = 11
            self.full_function_name()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == PythiaFunctionCallParser.T__1:
                self.state = 12
                self.match(PythiaFunctionCallParser.T__1)
                self.state = 13
                self.argument()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(PythiaFunctionCallParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Full_function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PythiaFunctionCallParser.STRING, 0)

        def getRuleIndex(self):
            return PythiaFunctionCallParser.RULE_full_function_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFull_function_name"):
                listener.enterFull_function_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFull_function_name"):
                listener.exitFull_function_name(self)

    def full_function_name(self):

        localctx = PythiaFunctionCallParser.Full_function_nameContext(self,
                                                                      self._ctx,
                                                                      self.state)
        self.enterRule(localctx, 2, self.RULE_full_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(PythiaFunctionCallParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(
                PythiaFunctionCallParser.ValueContext, 0)

        def getRuleIndex(self):
            return PythiaFunctionCallParser.RULE_argument

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArgument"):
                listener.enterArgument(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArgument"):
                listener.exitArgument(self)

    def argument(self):

        localctx = PythiaFunctionCallParser.ArgumentContext(self, self._ctx,
                                                            self.state)
        self.enterRule(localctx, 4, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return PythiaFunctionCallParser.RULE_array

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class ArrayOfValuesContext(ArrayContext):

        def __init__(self, parser,
                     ctx: ParserRuleContext):  # actually a PythiaFunctionCallParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    PythiaFunctionCallParser.ValueContext)
            else:
                return self.getTypedRuleContext(
                    PythiaFunctionCallParser.ValueContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArrayOfValues"):
                listener.enterArrayOfValues(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArrayOfValues"):
                listener.exitArrayOfValues(self)

    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser,
                     ctx: ParserRuleContext):  # actually a PythiaFunctionCallParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEmptyArray"):
                listener.enterEmptyArray(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEmptyArray"):
                listener.exitEmptyArray(self)

    def array(self):

        localctx = PythiaFunctionCallParser.ArrayContext(self, self._ctx,
                                                         self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0  # Token type
        try:
            self.state = 38
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                localctx = PythiaFunctionCallParser.ArrayOfValuesContext(self,
                                                                         localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(PythiaFunctionCallParser.T__0)
                self.state = 26
                self.value()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == PythiaFunctionCallParser.T__1:
                    self.state = 27
                    self.match(PythiaFunctionCallParser.T__1)
                    self.state = 28
                    self.value()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                self.match(PythiaFunctionCallParser.T__2)
                pass

            elif la_ == 2:
                localctx = PythiaFunctionCallParser.EmptyArrayContext(self,
                                                                      localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(PythiaFunctionCallParser.T__0)
                self.state = 37
                self.match(PythiaFunctionCallParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None,
                     invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return PythiaFunctionCallParser.RULE_value

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class IntegerContext(ValueContext):

        def __init__(self, parser,
                     ctx: ParserRuleContext):  # actually a PythiaFunctionCallParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(PythiaFunctionCallParser.INTEGER, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInteger"):
                listener.enterInteger(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInteger"):
                listener.exitInteger(self)

    class FloatContext(ValueContext):

        def __init__(self, parser,
                     ctx: ParserRuleContext):  # actually a PythiaFunctionCallParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PythiaFunctionCallParser.FLOAT, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFloat"):
                listener.enterFloat(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFloat"):
                listener.exitFloat(self)

    class StringContext(ValueContext):

        def __init__(self, parser,
                     ctx: ParserRuleContext):  # actually a PythiaFunctionCallParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PythiaFunctionCallParser.STRING, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterString"):
                listener.enterString(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitString"):
                listener.exitString(self)

    class ArrayValueContext(ValueContext):

        def __init__(self, parser,
                     ctx: ParserRuleContext):  # actually a PythiaFunctionCallParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(
                PythiaFunctionCallParser.ArrayContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArrayValue"):
                listener.enterArrayValue(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArrayValue"):
                listener.exitArrayValue(self)

    def value(self):

        localctx = PythiaFunctionCallParser.ValueContext(self, self._ctx,
                                                         self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 44
            token = self._input.LA(1)
            if token in [PythiaFunctionCallParser.T__0]:
                localctx = PythiaFunctionCallParser.ArrayValueContext(self,
                                                                      localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.array()

            elif token in [PythiaFunctionCallParser.STRING]:
                localctx = PythiaFunctionCallParser.StringContext(self,
                                                                  localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(PythiaFunctionCallParser.STRING)

            elif token in [PythiaFunctionCallParser.INTEGER]:
                localctx = PythiaFunctionCallParser.IntegerContext(self,
                                                                   localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(PythiaFunctionCallParser.INTEGER)

            elif token in [PythiaFunctionCallParser.FLOAT]:
                localctx = PythiaFunctionCallParser.FloatContext(self,
                                                                 localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(PythiaFunctionCallParser.FLOAT)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
