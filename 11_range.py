# Função range()

numeros = range(5) # range(5) = range(0, 5) = (0, 1, 2, 3, 4)
print(numeros)
for numero in numeros:
    print(numero)

numeros = range(5, 10) # range(5, 10) = range(5, 10) = (5, 6, 7, 8, 9)
print(numeros)
for numero in numeros:
    print(numero)

for numero in range(5, 10, 2): # o terceiro valor representa o passo de aumento da sequência
    print(numero)              # range(5, 10, 2) = (5, 7, 9)
