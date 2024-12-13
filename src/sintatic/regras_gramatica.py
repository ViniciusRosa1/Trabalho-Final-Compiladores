from ..lexer.analisador_lexico import Lexer
# Define-se os procedimentos associados as regras de
# produção da gramática (também é quando definimos a gramática)

#def p_<nome>(p):
#    '<não_terminal> : <TERMINAIS> <nao_terminais> ... ' 
#    <ações semânticas>
# -> ''' para regras com |

class RegrasGramatica:
    tokens = Lexer().regras_token.tokens
    # Definindo a precedência dos operadores
    precedencia = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'BITWISE_OR'),
        ('left', 'BITWISE_XOR'),
        ('left', 'BITWISE_AND'),
        ('left', 'COMPARATOR', 'NE'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MOD'),
        ('left', 'LSHIFT', 'RSHIFT'),
        ('right', 'INCREMENT', 'DECREMENT'),
        ('right', 'DOT'),
    )
    
    def __init__(self):
        pass
    #Reconhece o programa completo, incluindo diretivas do pré-processador, declarações e funções
    def p_programa(self,p):
        '''programa : diretiva_preprocessador_opcional lista_declaracao_opcional lista_funcoes'''
        print("Programa reconhecido")
        
    #Reconhece diretivas do pré-processador opcionais ou nenhuma diretiva 
    def p_diretiva_preprocessador_opcional(self, p):
        '''diretiva_preprocessador_opcional : lista_diretiva_preprocessador
                                                    | vazio'''
        print("lista diretiva preprocessador opcional reconhecida")                                           
    
    def p_lista_diretiva_preprocessador(self, p):
        '''lista_diretiva_preprocessador : diretiva_preprocessador'''
        print("lista diretiva preprocessador reconhecida")
        
    #Reconhece uma única diretiva do pré-processador - include ou define.
    def p_diretiva_preprocessador(self, p):
        '''diretiva_preprocessador : include_diretiva
                                      | define_diretiva'''
        print("Reconheceu uma única diretiva do pré-processador")
        
    #Reconhece uma diretiva include
    def p_include_diretiva(self, p):
        '''include_diretiva : HASH INCLUDE LIBRARY'''
        print("Reconheceu uma diretiva include")
        
    #Reconhece uma diretiva define
    def p_define_diretiva(self, p):
        '''define_diretiva : HASH DEFINE ID expressao
                            | HASH DEFINE ID'''
        print("Diretiva define reconhecida")
        
    #Reconhece uma lista opcional de declarações ou nenhuma declaração
    def p_lista_declaracao_opcional(self, p):
        '''lista_declaracao_opcional : lista_declaracao'''
        print("Reconheceu lista declaracao opcional")

    #Reconhece uma lista de declarações    
    def p_lista_declaracao(self, p):
        '''lista_declaracao : lista_declaracao declaracao
                              | vazio'''
        if len(p) == 3:
            print("Lista declaração extendida")
        else:
            print("Lista de declaracao vazia reconhecida")
            
    #Reconhece uma lista de funções
    def p_lista_funcoes(self, p):
        '''lista_funcoes : funcao
                          | lista_funcoes funcao'''
        print("Reconheceu uma lista de funções")
    
    #Reconhece uma definição de função, incluindo a função principal main        
    def p_funcao(self, p):
        '''funcao : funcao_main
                    | tipo_especificador ID LPAREN lista_parametros RPAREN declaracao_chaves
                    | tipo_especificador ID LPAREN RPAREN declaracao_chaves
                    '''
        print("Reconheceu uma definição de função")
        
    #	Reconhece a definição da função principal main.
    def p_funcao_main(self, p):
        '''funcao_main : tipo_especificador MAIN LPAREN RPAREN declaracao_chaves'''
        print("Reconheci main")

    #Reconhece uma lista de parâmetros de função
    def p_lista_parametros(self, p):
        '''lista_parametros : parametro
                              | lista_parametros COMMA parametro
                              | vazio'''
        print("Reconheceu uma lista de parâmetros de função")
    
    #Reconhece um parametro de função
    def p_parametro(self, p):
        '''parametro : tipo_especificador ID'''
        print("Reconheceu um parametro de função")
        
    # Reconhece um bloco de código delimitado por chaves {}   
    def p_declaracao_chaves(self, p):
        '''declaracao_chaves : LBRACE lista_instrucoes RBRACE'''
        print("Reconheceu um bloco de código delimitado por chaves")
    
    #Reconhece uma lista de instruções    
    def p_lista_instrucoes(self,p):
        '''lista_instrucoes : instrucao
                            | lista_instrucoes instrucao'''
        print("Reconheceu uma lista de instruções")
    
    #Reconhece uma única instrução, que pode ser de diversos tipos (declaração, atribuição, controle de fluxo)    
    def p_instrucao(self, p):
        '''instrucao :  declaracao
                        | atribuicao
                        | if_instrucao
                        | while_instrucao
                        | return_instrucao
                        | declaracao_chaves
                        | chamada_funcao SEMICOLON
                        | break_instrucao
                        | continue_instrucao
                        | for_instrucao
                        | switch_instrucao
                        | expressao SEMICOLON'''
        print("Instrucao reconhecida")
        
    #Reconhece uma declaração de variável, typedef ou struct
    def p_declaracao(self, p):
        '''declaracao : tipo_especificador init_lista_declarador SEMICOLON
                         | typedef_declaracao
                         | declaracao_struct'''
        print("Reconheceu declaracao")
        
    #Reconhece uma declaração typedef
    def p_typedef_declaracao(self, p):
        '''typedef_declaracao : TYPEDEF declaracao_struct'''
        print("Reconheceu declaracao typedef")
        
    #Reconhece uma declaração de struct   
    def p_declaracao_struct(self, p):
        '''declaracao_struct : STRUCT id_opcional LBRACE struct_membros RBRACE ID SEMICOLON'''
        print("Reconheceu declaracao struct")
        
    #Reconhece uma lista de membros de uma estrutura
    def p_struct_membros(self, p):
        '''struct_membros : struct_membro
                      | struct_membros struct_membro'''
        print("Reconheceu struct_membros")
        
    #conhece uma um membro de uma estrutura
    def p_struct_membro(self, p):
        '''struct_membro : tipo_especificador ID SEMICOLON'''
        print("Reconheceu struct") 
        
    #Reconhece um identificador opcional ou nenhum identificador
    def p_id_opcional(self, p):
        '''id_opcional : ID
                         | vazio'''
        print("Id opcional reconhecido")
        
    #Reconhece uma lista de inicializadores de declaradores    
    def p_init_lista_declarador(self, p):
        '''init_lista_declarador : init_declarador
                                   | init_lista_declarador COMMA init_declarador'''
        print("Reconheceu uma lista de inicializadores de declaradores")
    
    #Reconhece um inicializador de declarador
    def p_init_declarador(self, p):
        '''init_declarador : ID
                            | ID EQUALS expressao
                            | ID EQUALS LBRACE lista_inicializador RBRACE'''
        print("Reconheceu um inicializador de declarador")
    
    #Reconhece uma lista de inicializadores    
    def p_lista_inicializador(self, p):
        '''lista_inicializador : expressao
                                 | lista_inicializador COMMA expressao'''
        print("Reconheceu uma lista de inicializadores")
    
    #Reconhece um especificador de tipo
    def p_tipo_especificador(self, p):
        '''tipo_especificador : tipo_especificador_nao_vazio tipos_base
                                 | tipo_especificador_nao_vazio ID
                                 | ID'''
        if len(p) == 3:
            print("Reconheceu um especificador de tipo complexo")
        else:
            print("Reconheceu um especificador de tipo simples")
        
    
    #Reconhece um especificador de tipo não vazio       
    def p_tipo_especificador_nao_vazio(self, p):
        '''tipo_especificador_nao_vazio : tipo_previo_especificador'''
        print("Reconheceu um especificador de tipo não vazio")
    
    #Reconhece um tipo base (int, char, float)
    def p_tipos_base(self, p):
        ''' tipos_base : INT 
                    | CHAR 
                    | FLOAT
                    | DOUBLE
                    | VOID'''
        print("Tipos reconhecidos")
        
    # Reconhece um especificador de tipo prévio (const, long, ...)
    def p_tipo_previo_especificador(self, p):
        ''' tipo_previo_especificador : CONST
                                        | AUTO
                                        | VOLATILE
                                        | REGISTER
                                        | STATIC
                                        | UNSIGNED
                                        | SHORT
                                        | LONG
                                        | vazio'''
        print("Reconhece um especificador de tipo prévio")                            
    
    
    #Reconhece uma instrução de atribuição.
    def p_atribuicao(self,p):
        '''atribuicao : ID EQUALS expressao SEMICOLON'''
        print("Reconheceu atribuição")
    
    #Reconhece uma expressão, incluindo operações aritméticas e lógicas         
    def p_expressao(self,p):
        '''expressao : termo
                        | expressao PLUS termo
                        | expressao MINUS termo
                        | expressao LT termo
                        | expressao LE termo
                        | expressao GT termo
                        | expressao GE termo
                        | expressao NE termo
                        | expressao COMPARATOR termo
                        | expressao BITWISE_AND termo
                        | expressao BITWISE_OR termo
                        | expressao BITWISE_XOR termo
                        | expressao AND termo
                        | expressao OR termo
                        | expressao DOT ID
                        | expressao INCREMENT
                        | expressao DECREMENT
                        | chamada_funcao'''
        print("Expressao reconhecida")
     
    #Reconhece um termo em uma expressão aritmética    
    def p_termo(self,p):
        '''termo : fator
                   | termo TIMES fator
                   | termo DIVIDE fator
                   | termo MOD fator
                   | termo LSHIFT fator 
                   | termo RSHIFT fator'''
        print("Termo reconhecido")
    
    #Reconhece um fator em uma expressão, como um número ou uma variável        
    def p_fator(self, p):
        '''fator : INTEGER
                   | FLOAT_NUMBER
                   | STRING
                   | ID
                   | ID INCREMENT
                   | ID DECREMENT
                   | LPAREN expressao RPAREN'''
        print("Fator reconhecido")
        
    #Reconhece uma instrução if (condicional) 
    def p_if_instrucao(self, p):
        '''if_instrucao : IF fator instrucao
                        | IF fator instrucao ELSE instrucao'''
        print("IF reconhecido")
    
    #Reconhece uma instrução while (laço de repetição)        
    def p_while_instrucao(self, p):
        '''while_instrucao : WHILE fator instrucao'''
        print("While reconhecido")
    
    #Reconhece uma instrução for (laço de repetição)        
    def p_for_instrucao(self,p):
        '''for_instrucao : FOR LPAREN declaracao expressao SEMICOLON expressao RPAREN instrucao
                           | FOR LPAREN expressao SEMICOLON expressao SEMICOLON expressao RPAREN instrucao'''
        print("For reconhecido")
        
    #Reconhece uma instrução while (laço de repetição)
    def p_switch_instrucao(self,p):
        '''switch_instrucao : SWITCH fator LBRACE lista_case default_case RBRACE '''
        print("Switch reconhecido")

    #Reconhece uma lista de casos em uma instrução switch
    def p_lista_case(self, p):
        '''lista_case : case
                        | lista_case case
                        | vazio'''
        print("Lista case reconhecido")
    
    #Reconhece um caso em uma instrução switch.    
    def p_case(self, p):
        '''case : CASE expressao COLON lista_instrucoes'''
        print("Case reconhecido")

    #vReconhece o caso padrão em uma instrução switch        
    def p_default_case(self, p):
        '''default_case : DEFAULT COLON lista_instrucoes
                        | vazio'''
        print("Default case reconhecido")
    
    #Reconhece uma instrução break
    def p_break_instrucao(self,p):
        '''break_instrucao : BREAK SEMICOLON'''
        print("Reconheceu instrucao break")
    
    #Reconhece uma instrução continue        
    def p_continue_instrucao(self,p):
        '''continue_instrucao : CONTINUE SEMICOLON'''
        print("Continue instrução reconhecido")
    
    #Reconhece uma instrução return      
    def p_return_instrucao(self,p):
        '''return_instrucao : RETURN expressao SEMICOLON'''
        print("Return instrução reconhecido")

    #Reconhece uma chamada de função    
    def p_chamada_funcao(self,p):
        '''chamada_funcao : ID LPAREN RPAREN
                           | ID LPAREN lista_argumentos RPAREN'''
        print("Chamada de função reconhecida")

    #Reconhece uma lista de argumentos em uma chamada de função        
    def p_lista_argumentos(self, p):
        '''lista_argumentos : expressao
                             | lista_argumentos COMMA expressao'''
        print("Lista de argumentos reconhecida")
    
    def p_vazio(self, p):
        'vazio :'        

    #Função de tratamento de erros sintáticos
    def p_error(self,p):
        if p:
            print(f"Erro de sintaxe {p.value}, line {p.lineno}")
        else:
            print("Erro de sintaxe em EOF")
        
     
    


   