import os 
import sys
from src.lexer.analisador_lexico import Lexer
from src.sintatic.analisador_sintatico import Parser
from src.semantic.analisador_semantico import ParserSemantico

def analisador_lexico(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        codigo = file.read()
        
    lexer = Lexer()
    
    print("Tokens:")
    lexer.input(codigo)
    for token in lexer.tokenize():
        print(token)

def analisador_sintatico(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado")
        return
    with open(file_path, 'r', encoding='utf-8') as file:
        codigo = file.read()
    
    lexer = Lexer()
    parser = Parser()
    
    print("Tokens: ")
    lexer.input(codigo)
    for token in lexer.tokenize():
        print(token)
    
    print("\nParsing:")
    parser.parse(codigo)

def analisador_semantico(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado")
        return
    with open(file_path, 'r', encoding='utf-8') as file:
        codigo = file.read()
        
    lexer = Lexer()
    analise_semantica = ParserSemantico()
    
    print("Tokens:")
    lexer.input(codigo)
    for token in lexer.tokenize():
        print(token)
    
    print("\nParsing e analise Semantica:")
    analise_semantica.parse(codigo)
    
def main(file_path, mode):
    if mode == 'lexico':
        analisador_lexico(file_path)
    elif mode == 'sintatico':
        analisador_sintatico(file_path)
    elif mode == 'semantico':
        analisador_semantico(file_path)
    else:
        print("Modo inválido. As opções são lexico, sintatico e semantico")
    
        
if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Uso: python main.py <caminho_para_o_arquivo_c> <analisador>")