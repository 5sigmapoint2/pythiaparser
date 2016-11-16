# Generated from /Users/enrique/workspace/other/frontline/pythia/PythiaFunctionCall.g4 by ANTLR 4.5.3
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PythiaFunctionCallParser import PythiaFunctionCallParser
else:
    from PythiaFunctionCallParser import PythiaFunctionCallParser


# This class defines a complete listener for a parse tree produced by PythiaFunctionCallParser.
class PythiaFunctionCallListener(ParseTreeListener):
    # Enter a parse tree produced by PythiaFunctionCallParser#call.
    def enterCall(self, ctx: PythiaFunctionCallParser.CallContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#call.
    def exitCall(self, ctx: PythiaFunctionCallParser.CallContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#full_function_name.
    def enterFull_function_name(self,
                                ctx: PythiaFunctionCallParser.Full_function_nameContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#full_function_name.
    def exitFull_function_name(self,
                               ctx: PythiaFunctionCallParser.Full_function_nameContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#argument.
    def enterArgument(self, ctx: PythiaFunctionCallParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#argument.
    def exitArgument(self, ctx: PythiaFunctionCallParser.ArgumentContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#ArrayOfValues.
    def enterArrayOfValues(self,
                           ctx: PythiaFunctionCallParser.ArrayOfValuesContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#ArrayOfValues.
    def exitArrayOfValues(self,
                          ctx: PythiaFunctionCallParser.ArrayOfValuesContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#EmptyArray.
    def enterEmptyArray(self, ctx: PythiaFunctionCallParser.EmptyArrayContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#EmptyArray.
    def exitEmptyArray(self, ctx: PythiaFunctionCallParser.EmptyArrayContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#ArrayValue.
    def enterArrayValue(self, ctx: PythiaFunctionCallParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#ArrayValue.
    def exitArrayValue(self, ctx: PythiaFunctionCallParser.ArrayValueContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#String.
    def enterString(self, ctx: PythiaFunctionCallParser.StringContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#String.
    def exitString(self, ctx: PythiaFunctionCallParser.StringContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#Integer.
    def enterInteger(self, ctx: PythiaFunctionCallParser.IntegerContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#Integer.
    def exitInteger(self, ctx: PythiaFunctionCallParser.IntegerContext):
        pass

    # Enter a parse tree produced by PythiaFunctionCallParser#Float.
    def enterFloat(self, ctx: PythiaFunctionCallParser.FloatContext):
        pass

    # Exit a parse tree produced by PythiaFunctionCallParser#Float.
    def exitFloat(self, ctx: PythiaFunctionCallParser.FloatContext):
        pass
