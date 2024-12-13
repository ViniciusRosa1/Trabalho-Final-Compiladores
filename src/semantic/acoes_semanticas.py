from ..lexer.analisador_lexico import Lexer
from .regras_semantica import TabelaSimbolos

class RegrasSemantica:
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
        self.tabela_simbolos = TabelaSimbolos()
        self.struct_atual = None
        print("Tabela de símbolos inicializada")
        
    
    def p_programa(self,p):
        '''programa : diretiva_preprocessador_opcional lista_declaracao_opcional lista_funcoes'''
        print("Programa reconhecido")
        print(self.tabela_simbolos)
        
    def p_diretiva_preprocessador_opcional(self, p):
        '''diretiva_preprocessador_opcional : lista_diretiva_preprocessador
                                                    | vazio'''
        print("lista diretiva preprocessador opcional reconhecida")                                           
        
    def p_lista_diretiva_preprocessador(self, p):
        '''lista_diretiva_preprocessador : diretiva_preprocessador'''
        print("lista diretiva preprocessador reconhecida")
        
    
    def p_diretiva_preprocessador(self, p):
        '''diretiva_preprocessador : include_diretiva
                                      | define_diretiva'''
        print("Reconheceu uma única diretiva do pré-processador")
        
    
    def p_include_diretiva(self, p):
        '''include_diretiva : HASH INCLUDE LIBRARY'''
        print("Reconheceu uma diretiva include")
        
    def p_define_diretiva(self, p):
        '''define_diretiva : HASH DEFINE ID expressao
                            | HASH DEFINE ID'''
        print("Diretiva define reconhecida")
    
    def p_lista_declaracao_opcional(self, p):
        '''lista_declaracao_opcional : lista_declaracao'''
        print("Reconheceu lista declaracao opcional")

    def p_lista_declaracao(self, p):
        '''lista_declaracao : lista_declaracao declaracao
                              | vazio'''
        if len(p) == 3:
            print("Lista declaração extendida")
        else:
            print("lista de declaracao vazia reconhecida")


    def p_lista_funcoes(self, p):
        '''lista_funcoes : funcao
                          | lista_funcoes funcao'''
        print("Reconheceu uma lista de funções")
    

    def p_funcao(self, p):
        '''funcao : funcao_main
                    | tipo_especificador ID LPAREN lista_parametros RPAREN declaracao_chaves
                    | tipo_especificador ID LPAREN RPAREN declaracao_chaves
                    '''
        if len(p) == 6 or len(p) == 7:
            self.tabela_simbolos.add(p[2], p[1], p.lineno(2))
        self.tabela_simbolos.entra_escopo()
        print("Reconheceu uma definição de função")
        self.tabela_simbolos.sai_escopo()
        
    def p_funcao_main(self, p):
        '''funcao_main : tipo_especificador MAIN LPAREN RPAREN declaracao_chaves'''
        self.tabela_simbolos.add('main', p[1], p.lineno(2))
        self.tabela_simbolos.entra_escopo()
        print("Reconheceu funcao main")
        self.tabela_simbolos.sai_escopo()
        

    def p_lista_parametros(self, p):
        '''lista_parametros : parametro
                              | lista_parametros COMMA parametro
                              | vazio'''
        print("Reconheceu uma lista de parâmetros de função")
    

    def p_parametro(self, p):
        '''parametro : tipo_especificador ID'''
        self.tabela_simbolos.add(p[2], p[1], p.lineno(2))
        print("Reconheceu um parametro de função")
        
    def p_declaracao_chaves(self, p):
        '''declaracao_chaves : LBRACE lista_instrucoes RBRACE'''
        self.tabela_simbolos.entra_escopo()
        print("Reconheceu um bloco de código delimitado por chaves")
        self.tabela_simbolos.sai_escopo()
    
    def p_lista_instrucoes(self,p):
        '''lista_instrucoes : instrucao
                            | lista_instrucoes instrucao'''
        print("Reconheceu uma lista de instruções")
    
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
        print("instrucao reconhecida")
    
    def p_declaracao(self, p):
        '''declaracao : tipo_especificador init_lista_declarador SEMICOLON
                         | typedef_declaracao
                         | declaracao_struct'''
        print("Reconheceu declaracao")
        if len(p) == 4:
            for declarador in p[2]:
                self.tabela_simbolos.add(declarador['name'], p[1], p.lineno(1))
        
    def p_typedef_declaracao(self, p):
        '''typedef_declaracao : TYPEDEF declaracao_struct'''
        print("Reconheceu declaracao typedef")
        
    def p_declaracao_struct(self, p):
        '''declaracao_struct : STRUCT id_opcional LBRACE structs RBRACE ID SEMICOLON'''
        print("Reconheceu declaracao struct")
        struct_name = p[6]
        self.struct_atual = struct_name  # Definindo a estrutura atual antes de adicionar os membros
        self.tabela_simbolos.add(struct_name, 'struct', p.lineno(6))
        # Processo de membros da estrutura
        membros = p[4]
        for membro in membros:
            self.tabela_simbolos.add_struct_member(struct_name, membro['name'], membro['type'], membro['lineno'])
        self.struct_atual = None  # Redefinindo após adicionar a estrutura
    
    def p_structs(self, p):
        '''structs : struct 
                      | structs struct'''
        print("Reconheceu structs")
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]
            
    def p_struct(self, p):
        '''struct : tipo_especificador ID SEMICOLON'''
        info_membro = {'name': p[2], 'type': p[1], 'lineno': p.lineno(2)}
        p[0] = info_membro
        print("Reconheceu struct") 
    
    def p_id_opcional(self, p):
        '''id_opcional : ID
                         | vazio'''
        p[0] = p[1] if len(p) > 1 else ''
        print("Id opcional reconhecido")
        
    def p_init_lista_declarador(self, p):
        '''init_lista_declarador : init_declarador
                                   | init_lista_declarador COMMA init_declarador'''
        print("Reconheceu uma lista de inicializadores de declaradores")
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]
    
    def p_init_declarador(self, p):
        '''init_declarador : ID
                            | ID EQUALS expressao
                            | ID EQUALS LBRACE lista_inicializador RBRACE'''
        print("Reconheceu um inicializador de declarador")
        p[0] = {'name': p[1]}
    
    def p_lista_inicializador(self, p):
        '''lista_inicializador : expressao
                                 | lista_inicializador COMMA expressao'''
        print("Reconheceu uma lista de inicializadores")
    
    def p_tipo_especificador(self, p):
        '''tipo_especificador : tipo_especificador_nao_vazio tipos_base
                                 | tipo_especificador_nao_vazio ID
                                 | ID'''
        if len(p) == 3:
            p[0] = (p[1] if p[1] else '') + ' ' + p[2]
            print("Reconheceu um especificador de tipo complexo")
        else:
            p[0] = p[1]
            print("Reconheceu um especificador de tipo simples")
        
    
    def p_tipo_especificador_nao_vazio(self, p):
        '''tipo_especificador_nao_vazio : tipo_previo_especificador'''
        p[0] = p[1]
        print("Reconheceu um especificador de tipo não vazio")
    
    def p_tipos_base(self, p):
        ''' tipos_base : INT 
                    | CHAR 
                    | FLOAT
                    | DOUBLE
                    | VOID'''
        p[0] = p[1]
        print("Tipos reconhecidos")
        
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
        if p[1] == 'vazio':
            p[0] = ''
        else:
            p[0] = p[1]                                        
        print("Reconhece um especificador de tipo prévio")                            
    
    
    def p_atribuicao(self,p):
        '''atribuicao : ID EQUALS expressao SEMICOLON'''
        print("Reconheceu atribuiçao")
        var_info = self.tabela_simbolos.lookup(p[1])
        expr_type = p[3]['type'] if isinstance(p[3], dict) else self.get_type(p[3])
        if not self.are_types_compatible(var_info['type'], expr_type):
            raise Exception(f"Type error: Cannot assign '{expr_type}' to variable '{p[1]}' of type '{var_info['type']}'.")

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
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            if p.slice[2].type in ['INCREMENT', 'DECREMENT']:
                p[0] = self.tabela_simbolos.lookup(p[1])
        elif len(p) == 4:
            if p.slice[2].type == 'DOT':
                base_name = p[1]['name'] if isinstance(p[1], dict) else p[1]
                membro_name = p[3]
                struct_type = self.tabela_simbolos.lookup(base_name)['type']
                if struct_type not in self.tabela_simbolos.structs:
                    raise Exception(f"Error: '{base_name}' não é uma struct.")
                if membro_name not in self.tabela_simbolos.structs[struct_type]['members']:
                    raise Exception(f"Error: '{membro_name}' não é um membro da struct '{struct_type}'.")
                p[0] = self.tabela_simbolos.structs[struct_type]['members'][membro_name]
            else:
                left_type = self.get_type(p[1])
                right_type = self.get_type(p[3])
                if not self.are_types_compatible(left_type, right_type):
                    raise Exception(f"Type error: não executou a operação '{p[2]}' 3ntre '{left_type}' e '{right_type}'.")
                p[0] = {'type': left_type}
        print("Expressao reconhecida")
     
    def p_termo(self,p):
        '''termo : fator
                   | termo TIMES fator
                   | termo DIVIDE fator
                   | termo MOD fator
                   | termo LSHIFT fator 
                   | termo RSHIFT fator'''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            left_type = self.get_type(p[1])
            right_type = self.get_type(p[3])
            if not self.are_types_compatible(left_type, right_type):
                raise Exception(f"Type error: Cnão executou a operação '{p[2]}' entre '{left_type}' e '{right_type}'.")
            p[0] = {'type': left_type}
        print("termo reconhecido")
    
    
    def get_type(self, operand):
        if isinstance(operand, dict):
            return operand['type'].strip()  # Normaliza removendo espaços em branco
        elif isinstance(operand, str):
            var_info = self.symbol_table.lookup(operand)
            return var_info['type'].strip()  # Normaliza removendo espaços em branco
        else:
            return type(operand).__name__.lower()
    
    def are_types_compatible(self, type1, type2):
        # Normaliza removendo espaços em branco
        type1 = type1.strip()
        type2 = type2.strip()

        # Tipos são compatíveis se forem exatamente iguais
        if type1 == type2:
            return True

        # Definindo conjuntos de tipos compatíveis
        int_types = {'int', 'unsigned int', 'short', 'unsigned short', 'long', 'unsigned long'}
        float_types = {'float', 'double', 'long double'}
        char_types = {'char', 'unsigned char', 'signed char'}

        # Verificação de compatibilidade entre tipos inteiros
        if type1 in int_types and type2 in int_types:
            return True

        # Verificação de compatibilidade entre tipos de ponto flutuante
        if type1 in float_types and type2 in float_types:
            return True

        # Verificação de compatibilidade entre tipos de caracteres
        if type1 in char_types and type2 in char_types:
            return True

        # Compatibilidade entre tipos inteiros e float (conversão implícita permitida)
        if (type1 in int_types and type2 in float_types) or (type1 in float_types and type2 in int_types):
            return True

        # Caso contrário, os tipos não são compatíveis
        return False
    
    def p_fator(self, p):
        '''fator : INTEGER
                   | FLOAT_NUMBER
                   | STRING
                   | ID
                   | ID INCREMENT
                   | ID DECREMENT
                   | LPAREN expressao RPAREN'''
        if len(p) == 2:
            if p.slice[1].type == 'ID':
                p[0] = self.tabela_simbolos.lookup(p[1])
            elif p.slice[1].type == 'INTEGER':
                p[0] = {'type': 'int'}
            elif p.slice[1].type == 'FLOAT_NUMBER':
                p[0] = {'type': 'float'}
            elif p.slice[1].type == 'STRING':
                p[0] = {'type': 'char'}  # Assumindo que strings são tratadas como arrays de chars
        elif len(p) == 3:
            p[0] = self.tabela_simbolos.lookup(p[1])
        elif len(p) == 4:
            p[0] = p[2]
        print("Fator reconhecido")
        
    def p_if_instrucao(self, p):
        '''if_instrucao : IF fator instrucao
                        | IF fator instrucao ELSE instrucao'''
        print("IF reconhecido")
    
    def p_while_instrucao(self, p):
        '''while_instrucao : WHILE fator instrucao'''
        print("While reconhecido")
    
    def p_for_instrucao(self,p):
        '''for_instrucao : FOR LPAREN declaracao expressao SEMICOLON expressao RPAREN instrucao
                           | FOR LPAREN expressao SEMICOLON expressao SEMICOLON expressao RPAREN instrucao'''
        print("For reconhecido")
        
    def p_switch_instrucao(self,p):
        '''switch_instrucao : SWITCH fator LBRACE lista_case default_case RBRACE '''
        print("Switch reconhecido")

    def p_lista_case(self, p):
        '''lista_case : case
                        | lista_case case
                        | vazio'''
        print("Lista case reconhecido")
    
    def p_case(self, p):
        '''case : CASE expressao COLON lista_instrucoes'''
        print("Case reconhecido")

    def p_default_case(self, p):
        '''default_case : DEFAULT COLON lista_instrucoes
                        | vazio'''
        print("default case reconhecido")
    
    def p_break_instrucao(self,p):
        '''break_instrucao : BREAK SEMICOLON'''
    
    def p_continue_instrucao(self,p):
        '''continue_instrucao : CONTINUE SEMICOLON'''
        print("Continue instrução reconhecido")
    
    def p_return_instrucao(self,p):
        '''return_instrucao : RETURN expressao SEMICOLON'''
        print("Return instrução reconhecido")

    def p_chamada_funcao(self,p):
        '''chamada_funcao : ID LPAREN RPAREN
                           | ID LPAREN lista_argumentos RPAREN'''
        self.tabela_simbolos.lookup(p[1])
        print("Chamada de função reconhecida")

    def p_lista_argumentos(self, p):
        '''lista_argumentos : expressao
                             | lista_argumentos COMMA expressao'''
        print("Lista de argumentos reconhecida")
    
    def p_vazio(self, p):
        'vazio :'        

    def p_error(self,p):
        if p:
            print(f"Erro de sintaxe {p.value}, line {p.lineno}")
        else:
            print("Erro de sintaxe em EOF")
        
     
    


   