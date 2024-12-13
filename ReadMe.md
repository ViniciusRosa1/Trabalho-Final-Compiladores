### Clonar o Repositório

```bash
git clone https://github.com/ViniciusRosa1/Trabalho-Final-Compiladores.git
cd Trabalho-Final-Compiladores
```

### Configurar o Ambiente Virtual

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executando os Analisadores

### Executando o Analisador Léxico

Para executar o analisador léxico em um arquivo C:

```bash
python main.py <test/caso1.c> lexico
```

### Executando o Analisador Sintático

Para executar o analisador sintático em um arquivo C:

```bash
python main.py <test/caso1.c> sintatico
```

### Executando o Analisador Semântico

Para executar o analisador semântico em um arquivo C:

```bash
python main.py <test/caso1.c> semantico
```
