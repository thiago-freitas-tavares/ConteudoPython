# Exercício 2 - Análise de Crédito

preco = 1_000_000
bom_credito = True
if bom_credito:
    sinal = 0.1
else:
    sinal = 0.2
print(f"Sinal = R$ {int(preco*sinal)}")
print("Sinal necessário de " + str(sinal*100) + " % = R$ "+ str(int(preco*sinal)))
print("Sinal necessário de",sinal*100,"% = R$",int(preco*sinal))
