// ----------------------------------------------------------------------------
// Grammars always start with a grammar header. This grammar is called
// PythiaFunctionCall and must match the filename: PythiaFunctionCall.g4
// ----------------------------------------------------------------------------
grammar PythiaFunctionCall;

call
    :   '[' full_function_name ( ',' argument )* ']'
    ;

full_function_name
    :   STRING
    ;

argument
    :   value
    ;

array
    :   '[' value ( ',' value )* ']'    # ArrayOfValues
    |   '[' ']'                         # EmptyArray
    ;

value
    :   array   # ArrayValue
    |   STRING  # String
    |   INTEGER # Integer
    |   FLOAT   # Float
    ;

// ----------------------------------------------------------------------------
// Lexer
// Parser rules start with lowercase letters, lexer rules with uppercase
// ----------------------------------------------------------------------------

STRING
    :   QUOTE ( ESCAPED_QUOTE | ~ '\'' )* QUOTE
    ;

INTEGER
    :   '-'? INT            // -3, 45
    ;

FLOAT
    :   '-'? INT '.' INT    // 1.35, 0.3, -4.5
    ;

fragment
QUOTE
    :   '\''
    ;

fragment
ESCAPED_QUOTE
    :   '\\\''
    ;

fragment
INT
    : '0' | '1'..'9' '0'..'9'*  // no leading zeros
    ;

WS
    :   [ \t\n\r]+ -> skip
    ;
