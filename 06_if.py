# Operador de Condição

temperatura = 9

if temperatura > 30:            # (30+)
    print("É um dia quente")
elif temperatura > 20:          # (20 a 30)
    print("É um dia agradável")
elif temperatura > 10:          # (10 a 20)
    print("É um dia frio")
else:                           # (10-)
    print("É um dia gelado")
print("Fim")

is_hot = True
is_cold = True

if is_hot:
    print("É um dia quente")
elif is_cold:
    print("É um dia frio")
else:
    print("É um dia agradável")
print("Fim")
