# Operador de Iteração

# Lista

numeros = [1, 2, 3, 4, 5]

for item in numeros: # item é uma variável de loop (pode ter qualquer nome) e não precisa ser declarada.
    print(item) # imprimir na vertical

for item in 'Python':
    print(item)

# função range() cria um objeto, que não é uma lista, mas algo similar, que pode sofrer iteração
for item in range(5, 10, 2):
    print(item)

i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1
