# Exercício 7 - Remover Duplicatas em uma Lista

numeros = [2, 2, 4, 6, 3, 4, 6, 1]
unicas = numeros.copy()
print(numeros)

for item in numeros:                    # 0 in numeros = 2 -> item = 2 | # 1 in numeros = 2 -> item = 2
                                          # 2 in numeros = 4 -> item = 4 | # 3 in numeros = 6 -> item = 6
    qtd = unicas.count(item)      # qtd = 2 | # qtd = 1 | # qtd = 2 | # qtd = 2
    if qtd > 1:                         # 2 > 1 SIM | # 1 > 1 NAO | # 2 > 1 SIM | # 2 > 1 SIM
        for l in range(qtd-1):          # 0 in range(1) = 0 -> l = 0 | # 1 in range(1) = 1 -> l = X
                                          # 0 in range(1) = 0 -> l = 0 | # 1 in range(1) = X
            unicas.remove(item)   # remove primeiro 2 | # remove primeiro 4 | # remove primeiro 6
                                          # [2, 4, 6, 3, 4, 6, 1] | [2, 6, 3, 4, 6, 1] | [2, 3, 4, 6, 1]
print(unicas)                     # [2, 3, 4, 6, 1]

# Solução mais Simplificada

numeros = [2, 2, 4, 6, 3, 4, 6, 1]
unicas = []
print(numeros)

for item in numeros:
    if item not in unicas:
        unicas.append(item)
print(unicas)