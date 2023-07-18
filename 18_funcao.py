# Função
# É um pacote que armazena algumas linhas de código que realizam uma tarefa específica.
# print() e input() são exemplos de funções básicas.

def comprimentar():             # def = define -> cria função
    print('Olá,')
    print('Bem vindo a bordo!')

print('Início')
comprimentar()
print('Fim')

# Parâmetros de Função


def comprimentar(nome):         # Podemos definir parâmetros que funcionam como ponte para passar informação
    print(f'Olá, {nome}.')      # para dentro da função ao chamá-la.
    print('Bem vindo a bordo!')


n1 = input('Digite seu nome: ')
n2 = input('Digite seu nome: ')
print('Início')
comprimentar(n1)                # n1 e n2 são argumentos passados para a função através do parâmetro nome.
comprimentar(n2)
print('Fim')


def comprimentar(primeiro_nome, sobrenome):
    print(f'Olá, {primeiro_nome} {sobrenome}.')
    print('Bem vindo a bordo!')


n1 = input('Digite seu nome: ')
n2 = input('Digite seu sobrenome: ')
print('Início')
comprimentar(n1, n2)
print('Fim')
