class TabelaSimbolos:
    """
    A classe TabelaSimbolos gerencia as variáveis e seus escopos dentro do programa.
    Ela permite adicionar novas variáveis, buscar variáveis existentes e gerenciar
    os diferentes escopos (global e locais) durante a execução do programa.
    """
    def __init__(self):
        self.escopo_global = {}
        self.stack_escopo_local = []
        self.funcoes_padrao = {'printf', 'scanf'}
    
    def entra_escopo(self):
        #Entra em um novo escopo local, adicionando um dicionário vazio à pilha de escopos locais.
        self.stack_escopo_local.append({})
    
    def sai_escopo(self):
        #Sai do escopo local atual, removendo o dicionário do topo da pilha de escopos locais.
        self.stack_escopo_local.pop()
    
    def add(self, name, type_, lineno):
        """
        Adiciona uma nova variável à tabela de símbolos no escopo atual.
        
        Parâmetros:
        - name (str): Nome da variável.
        - type_ (str): Tipo da variável.
        - lineno (int): Número da linha onde a variável foi declarada.
        """
        
        escopo = self.stack_escopo_local[-1] if self.stack_escopo_local else self.escopo_global
        if name in escopo:
            raise Exception(f"Erro: Variável '{name}' já declarada na linha {lineno}.")
        escopo[name] = {'type': type_, 'lineno': lineno}
    
    def lookup(self, name):
        """
        Procura uma variável na tabela de símbolos, começando pelo escopo mais interno até o global.
        Retorna as informações da variável se encontrada e lança uma exceção se a variável não foi declarada.
        """
        for escopo in reversed(self.stack_escopo_local):
            if name in escopo:
                return escopo[name]
        
        if name in self.escopo_global:
            return self.escopo_global[name]
        if name in self.funcoes_padrao:
            return {'type': 'function', 'lineno': -1}
        raise Exception(f"Erro: Variável '{name}' usada sem declaração.")
    
    def __str__(self):
        #Retorna uma representação em string do escopo global da tabela de símbolos.

        return str(self.escopo_global)
            