class RegrasToken:
    def __init__(self):
        self.reserved = {
        'if' : 'IF',
        'else' : 'ELSE',
        'for' : 'FOR',
        'while' : 'WHILE',
        'switch':'SWITCH',
        'case' : 'CASE',
        'break' : 'BREAK',
        'continue' : 'CONTINUE',
        'include' : 'INCLUDE',
        'int' : 'INT',
        'float' : 'FLOAT',
        'char' : 'CHAR',
        'double' : 'DOUBLE',
        'const' : 'CONST',
        'auto' : 'AUTO',
        'enum' : 'ENUM',
        'long' : 'LONG',
        'default' : 'DEFAULT',
        'unsigned' : 'UNSIGNED',
        'return' : 'RETURN',
        'register' : 'REGISTER',
        'static' : 'STATIC',
        'short'  : 'SHORT',
        'volatile' : 'VOLATILE',
        'void' : 'VOID',
        'sizeof' : 'SIZEOF',
        'define' : 'DEFINE',
        'struct' : 'STRUCT',
        'typedef' : 'TYPEDEF',
        }
        
        self.tokens = [
            'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MOD', 'INCREMENT', 'DECREMENT',
            'LT', 'LE', 'GT', 'GE', 'NE', 'COMPARATOR',
            'EQUALS', 'AND', 'OR', 'NOT',
            'BITWISE_AND', 'BITWISE_OR', 'BITWISE_XOR', 'LSHIFT', 'RSHIFT', 'BITWISE_NOT',
            'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON', 'COLON', 'NEWLINE',
            'INTEGER', 'FLOAT_NUMBER', 'STRING', 'ID', 'MAIN', 'LIBRARY',
            'TERNARY', 'ARROW', 'DOT', 'HASH', 'DOUBLEHASH'
        ] + list(self.reserved.values())
        
    t_ignore = ' \t'

    
        # Define novas linhas
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Define o token de função principal
    def t_MAIN(self, t):
        r'main'
        return t

    # Define o identificador
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value,'ID')
        return t

    # Define o token de número flutuante
    def t_FLOAT_NUMBER(self, t):
        r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
        t.value = float(t.value)
        return t

    # Define o token de biblioteca
    def t_LIBRARY(self, t):
        r'[<][a-zA-Z_][a-zA-Z0-9_]*\.h[>]'
        return t

    # Define o token de string entre aspas duplas
    def t_STRING(self, t):
        r'\"([^\\\n]|(\\.))*?\"'
        return t
    
    
    t_EQUALS = r'='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_POWER = r'\^'
    t_INCREMENT = r'\+\+'
    t_DECREMENT = r'--'
    t_MOD = r'%'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_RBRACE = r'\}'
    t_LBRACE = r'\{'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_SEMICOLON = r'\;'
    t_TERNARY = r'\?'
    t_DOT = r'\.'
    t_ARROW = r'->'
    t_COLON = r':'
    t_HASH = r'\#'
    t_DOUBLEHASH = r'\#\#'

    t_LT = r'<'
    t_LE = r'<='
    t_GT = r'>'
    t_GE = r'>='
    t_NE = r'!='
    t_COMPARATOR = r'=='
    t_BITWISE_AND = r'&'
    t_BITWISE_OR = r'\|'
    t_BITWISE_XOR = r'\^'
    t_BITWISE_NOT = r'~'
    t_LSHIFT = r'<<'
    t_RSHIFT = r'>>'

    t_AND = r'&&'
    t_OR = r'\|\|'
    t_NOT = r'!'

    t_COMMA = r'\,'
    t_INTEGER = r'\d+'
    
    # Ignora comentários de uma linha ou multiplas linhas
    def t_COMMENT(self, t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        t.lexer.lineno += t.value.count('\n')
        
    def t_error(self, t):
        print("Illegal character %s" % t.value[0])
        t.lexer.skip(1)