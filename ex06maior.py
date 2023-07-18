# Exercício 6 - Maior Número de uma Lista

numeros = [25, 3, 54, 34, 35, 16]

max = numeros[0]    # max = 25
for n in numeros:   # 0 in numeros = 25 -> n = 25 | # 1 in numeros = 3 -> n = 3 |...| # 5 in numeros = 16 -> n = 16
    if n > max:     # 25 > 25 NAO | # 3 > 25 NAO |...| # 16 > 54 NAO
        max = n     # max = 54
print(max)

# A variável max fica sublinhada em amarelo (Shadows built-in name),
# pois por padrão existe uma função max da linguagem Python, que faz exatamente o que nossa função achar_max faz.
