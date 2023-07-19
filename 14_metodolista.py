# Métodos

# Métodos de Lista

# * ctrl+p te mostra os parâmetros do Método.

numeros = [7, 4, 6, 9, 2]
print(numeros)
numeros.sort()              # ordena os itens da lista em ordem crescente.
print(numeros)
numeros.reverse()           # inverte a ordem dos itens na lista (se estava crescente, passa a ficar decrescente).
print(numeros)

numero2 = numeros.copy()
print(numero2)

numeros.append(5)           # adiciona o item desejado no final da lista.
print(numeros)

numeros.insert(0, 2)        # insere o item desejado (2) na posição desejada (0).
print(numeros)
print(len(numeros))

print(numeros.index(9))     # devolve a posição do item desejado. Caso o item não esteja na lista, da um erro.
print(50 in numeros)        # devolve true ou false se o item desejado encontra-se na lista ou não.
print(numeros.count(2))     # devolve a qtd de vezes que o item desejado aparece ha lista.

numeros.remove(6)           # o primeiro número está na posição 1, neste caso não existe posição zero.
print(numeros)
numeros.remove(2)           # remove o item desejado somente na  primeira vez que ele aparecer.
print(numeros)

numeros.pop()               # remove o último item da lista.
numeros.pop()
print(numeros)

print(1 in numeros)
print(7 in numeros)

numeros.clear()
print(numeros)
