# Exercício 1 - Conversão de Peso

peso = float(input("Peso: "))
unidade = input("(K)g ou (L)b: ")
# if unidade == "K" or unidade == "k":
if unidade.upper() == "K":
    convertido = peso * 2.20462
    print("Peso em Lb:", convertido)
else:
    convertido = peso / 2.20462
    print("Peso em Kg:" + str(convertido))
print("Fim")
