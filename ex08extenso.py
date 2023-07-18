# Exercício 8 - Números por Extenso

fone = input("Telefone: ")      # Salvo como string

conversao = {
    "1": "um",
    "2": "dois",
    "3": "três",
    "4": "quatro",
    "5": "cinco",
    "6": "seis",
    "7": "sete",
    "8": "oito",
    "9": "nove"
}
extenso = ""
for n in fone:
    extenso += conversao.get(n, "!") + " "
print(extenso)

# Solução sem usar Dicionário

'''
i = 0
extenso = []
for n in fone:
    if int(n) == 0:
        extenso.append("zero")
    elif int(n) == 1:
        extenso.append("um")
    elif int(n) == 2:
        extenso.append("dois")
    elif int(n) == 3:
        extenso.append("três")
    elif int(n) == 4:
        extenso.append("quatro")
    elif int(n) == 5:
        extenso.append("cinco")
    elif int(n) == 6:
        extenso.append("seis")
    elif int(n) == 7:
        extenso.append("sete")
    elif int(n) == 8:
        extenso.append("oito")
    elif int(n) == 9:
        extenso.append("nove")
    else:
        print(n)
    i += 1
print(extenso)
'''
