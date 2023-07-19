# Lidando com Erros (try / except)

try:
    idade = int(input('Idade: '))
    constante = 1000
    risco = constante / idade
    print(risco)
except ValueError and ZeroDivisionError:
    print('Entrada Inválida!')


# Idade: asd
#     idade = int(input('Idade: '))
# ValueError: invalid literal for int() with base 10: '32k'
#
# Process finished with exit code 1

# Idade: 0
#     risco = constante / idade
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1
