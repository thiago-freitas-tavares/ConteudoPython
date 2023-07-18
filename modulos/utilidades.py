def achar_max(numeros):
    max = numeros[0]
    for n in numeros:
        if n > max:
            max = n
    return max

# A variável max fica sublinhada em amarelo (Shadows built-in name),
# pois por padrão existe uma função max da linguagem Python, que faz exatamente o que nossa função achar_max faz.

def calc_frete():
    print('Cálculo do Frete: ')
