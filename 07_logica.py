# Operadores de Lógica

price = 5
print(price > 10 and price < 30)
print(price > 10 or price < 30)
print(not price > 10)

salario_alto = True
bom_credito = False
antecedente_criminal = False
if salario_alto or bom_credito and not antecedente_criminal:
    print("Elegível para empréstimo.")
else:
    print("Não elegível para empréstimo.")
