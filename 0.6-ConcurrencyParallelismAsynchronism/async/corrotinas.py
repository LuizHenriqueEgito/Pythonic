# Decorador para preparar corrotinas automaticamente
def corrotina(func):
    def start(*args, **kwargs):
        coro = func(*args, **kwargs)  # Cria a corrotina
        next(coro)                    # Avança até o primeiro yield
        return coro                    # Retorna a corrotina pronta
    return start

# Corrotina que apenas imprime o que recebe
@corrotina
def printer():
    while True:
        value = yield                # Espera receber um valor
        print("Recebido:", value)    # Imprime o valor recebido

# Corrotina que filtra valores que contêm a palavra 'spam'
@corrotina
def grep(target):
    while True:
        item = yield                  # Espera receber um valor
        if 'spam' in item:            # Se a palavra 'spam' estiver presente
            target.send(item)         # Envia para a próxima corrotina

# Corrotina que substitui 'spam' por 'bacon'
@corrotina
def replace(target):
    while True:
        item = yield                  # Recebe uma string
        novo = item.replace('spam', 'bacon')  # Substitui
        target.send(novo)             # Envia para o próximo alvo

# Criando as corrotinas e ligando-as
p = printer()         # corrotina final que imprime
r = replace(p)        # corrotina que substitui e envia para printer
g = grep(r)           # corrotina que filtra 'spam' e envia para replace

# Dados de teste
dados = ['spam', 'hello spam', 'eggs']

# Enviando dados para a primeira corrotina
for linha in dados:
    g.send(linha)
