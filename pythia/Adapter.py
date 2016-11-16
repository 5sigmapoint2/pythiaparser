import importlib
import sys
import traceback

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import ParseTreeWalker

from pythia.antlr4.PythiaFunctionCallLexer import PythiaFunctionCallLexer
from pythia.antlr4.PythiaFunctionCallListener import PythiaFunctionCallListener
from pythia.antlr4.PythiaFunctionCallParser import PythiaFunctionCallParser


# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
class FunctionCall(PythiaFunctionCallListener):
    def __init__(self):
        self.module_name = ""
        self.function_name = ""
        self.function_fqn = ""
        self.args = ()
        self.mem = {}

    def exitCall(self, ctx: PythiaFunctionCallParser.CallContext):
        self.args = tuple(self.mem[arg_ctx] for arg_ctx in ctx.argument())

    def exitFull_function_name(self,
                               ctx: PythiaFunctionCallParser.Full_function_nameContext):
        self.function_fqn = ctx.getText().strip('\'')
        self.module_name, self.function_name = self.function_fqn.rsplit('.', 1)

    def exitArgument(self, ctx: PythiaFunctionCallParser.ArgumentContext):
        self.mem[ctx] = self.mem[ctx.value()]

    def exitArrayOfValues(self,
                          ctx: PythiaFunctionCallParser.ArrayOfValuesContext):
        self.mem[ctx] = [self.mem[value_ctx] for value_ctx in ctx.value()]

    def exitEmptyArray(self, ctx: PythiaFunctionCallParser.EmptyArrayContext):
        self.mem[ctx] = []

    def exitArrayValue(self, ctx: PythiaFunctionCallParser.ArrayValueContext):
        self.mem[ctx] = self.mem[ctx.array()]

    def exitString(self, ctx: PythiaFunctionCallParser.StringContext):
        self.mem[ctx] = ctx.getText().strip('\'')

    def exitInteger(self, ctx: PythiaFunctionCallParser.IntegerContext):
        self.mem[ctx] = int(ctx.getText())

    def exitFloat(self, ctx: PythiaFunctionCallParser.FloatContext):
        self.mem[ctx] = float(ctx.getText())


# ----------------------------------------------------------------------------
# The Extension entry point in python
# ----------------------------------------------------------------------------
def python_adapter(input_string):
    try:
        if input_string == "":
            return format_error_string("Input string cannot be empty")

        call = parse_input(input_string)

        return_value = python_proxy(
            call.module_name,
            call.function_name,
            call.function_fqn,
            *call.args)

        return format_response_string(return_value)

    except:
        return format_error_string(traceback.format_exc())


# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
def parse_input(input_string):
    input = InputStream(input_string)
    function_call = FunctionCall()

    walker = ParseTreeWalker()
    walker.walk(
        function_call,
        PythiaFunctionCallParser(
            CommonTokenStream(
                PythiaFunctionCallLexer(input))).call())

    return function_call


# ----------------------------------------------------------------------------
# Performs the call
# ----------------------------------------------------------------------------
def python_proxy(module_name, function_name, function_fqn, *args):
    global FUNCTION_CACHE

    try:
        function = FUNCTION_CACHE[function_fqn]

    except KeyError:  # Function not cached, load the module
        try:
            module = sys.modules[module_name]

        except KeyError:
            # Module not imported yet, import it
            module = importlib.import_module(module_name)

        # Get the requested function
        function = getattr(module, function_name)
        FUNCTION_CACHE[function_fqn] = function

    # Call the requested function with the given arguments
    return function(*args)


# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
def format_error_string(stacktrace_str):
    """Return a formatted exception."""
    return '["e", "{}"]'.format(stacktrace_str.replace('"', '""'))


# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
def format_response_string(return_value):
    """Return a formatted response.
    For now, it's just doing a dumb str() which may or may not work depending
    on the arguments passed. This should work as long as none of the arguments
    contain double quotes (").
    """

    return str(["r", return_value])


###############################################################################
# Below are testing functions which exist solely to check if everything is
# working correctly.
# If someone wants to check if their python module works, they should Call
# Pythia.test() and later Pythia.ping() to make sure they understand the syntax
###############################################################################

def test(*args):
    return "OK"


def ping(*args):
    return list(args)


FUNCTION_CACHE = {
    'Pythia.ping': ping,
    'Pythia.test': test,
}

# Somehow Visual Studio cannot load this if there is a newline at The
# end of the file
