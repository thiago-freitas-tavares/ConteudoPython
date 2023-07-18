# Argumentos Posicionais e Argumentos Palavra Chave

# Utilizando o exemplo do conteúdo anterior:
def comprimentar(primeiro_nome, sobrenome):
    print(f'Olá, {primeiro_nome} {sobrenome}.')
    print('Bem vindo a bordo!')

n1 = input('Digite seu nome: ')
n2 = input('Digite seu sobrenome: ')
print('Início')
comprimentar(n1, n2)                            # desta forma (Positional Argument) a ordem dos argumentos importa.
comprimentar(sobrenome=n2, primeiro_nome=n1)    # desta forma (keyword Argument) a ordem dos argumentos NÃO importa.
print('Fim')

# Em um exemplo que tenha uma função para calcular o valor final de uma nota fiscal, na chamada da função,
# poderia usar positional argument, mas o keyword argument torna a leitura do código mais fácil.

# calculo(total=50, frete=5, desconto=0.1)

# Para utilizar um mix de positional e keyword arguments o primeiro argumento deve ser posicional, senão da erro.

# calculo(total=50, 5, desconto=0.1)  # Erro
# calculo(50, frete=5, 0.1)           # Erro
# calculo(50, frete=5, desconto=0.1)  # Ok
