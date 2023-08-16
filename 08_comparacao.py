# Operadores de Comparação

x = 5 > 3
print(x)
x = 5 >= 2
print(x)
x = 5 < 8
print(x)
x = 5 <= 5
print(x)
x = 5 == 7
print(x)
x = 5 != 7
print(x)

name = input("Digite seu nome completo: ")
if len(name) < 3:
    print("Nome deve ter no mínimo 3 caracteres.")
elif len(name) > 10:
    print("Nome deve ter no máximo 10 caracteres")
else:
    print("Cadastro realizado com sucesso.")
