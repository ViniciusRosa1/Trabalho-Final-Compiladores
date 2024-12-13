from ply import yacc
from ..lexer.analisador_lexico import Lexer
from .acoes_semanticas import RegrasSemantica

class ParserSemantico:
    def __init__(self):
        
        self.lexer = Lexer()
        self.grammar = RegrasSemantica()
        self.tokens = self.lexer.regras_token.tokens
        self.parser = yacc.yacc(module=self.grammar)
        
    def parse(self, data):
        
        self.lexer.input(data)
        return self.parser.parse(lexer=self.lexer.lexer)
    
    def p_error(p):
        """
        Função de tratamento de erros sintáticos.

        Parâmetros:
        - p: Token onde o erro ocorreu.

        Imprime a mensagem de erro com o valor e a linha do token onde o erro ocorreu.
        Se p for None, indica que o erro ocorreu no final do arquivo.
        """
        if p:
            print(f"Erro sintático em '{p.value}', linha {p.lineno}")
        else:
            print("Erro sintático no final do arquivo (EOF)")