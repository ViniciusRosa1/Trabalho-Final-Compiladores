# ATIVIDADE PRÁTICA - reconhecedor de estruturas em C
from ply import yacc
from .regras_gramatica import RegrasGramatica
from ..lexer.analisador_lexico import Lexer

class Parser:
    """
    A classe Parser configura e utiliza o analisador sintático (parser) para analisar
    o código fonte de acordo com as regras definidas na classe RegrasGramatica.
    """
    def __init__(self):
        """Função para inicializar a classe parser. Cria instância do Lexer e das RegrasGramatica, 
        configura os tokens e cria o parser utilizando a biblioteca PLY"""
        self.lexer = Lexer()
        self.regras = RegrasGramatica()
        self.tokens = self.lexer.regras_token.tokens
        self.parser=yacc.yacc(module=self.regras)
    
    def parse(self, data):
        """Método para analisar o código fonte fornecido"""
        self.lexer.input(data)
        return self.parser.parse(lexer=self.lexer.lexer)

    def p_error(p):
        """Função de tratamento de erros sintáticos"""
        if p:
            print(f"Erro de sintaxe {p.value}, line {p.lineno}")
        else:
            print("Erro de sintaxe em EOF")

