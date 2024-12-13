from ply import lex
from .regras_token import RegrasToken

class Lexer:
    """
    Classe Lexer configura e utiliza o analisador léxico (lexer) para converter 
    o código fonte em tokens utilizando a classe RegrasToken.
    """
    def __init__(self):
        """
        Função para iniciar a classe Lexer. Cria uma instância de TokenRules e configura
        o lexer.
        """
        self.regras_token = RegrasToken()
        self.lexer = lex.lex(module=self.regras_token)
    
    def input(self, data):
        """Função para inserir código fonte ao lexer"""
        self.lexer.input(data)

    def token(self):
        """Função para obter o próximo token ao lexer"""
        return self.lexer.token()
   
    def tokenize(self):
        """Função que gera uma sequência de tokens a partir do código fonte fornecido"""
        while True:
            tok = self.token()
            if not tok:
                break
            yield tok
