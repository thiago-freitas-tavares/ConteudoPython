# Tuple (lista imutável - entre parênteses)

numeros = (1, 2, 2, 3, 3, 3)

# Não dá para modificar um tuple, eles são imutáveis.
# numeros[0] = 10 não funciona.

print(numeros.count(3))
print(numeros.index(2))     # mostra a primeira posição do número ou item indexado.
print(numeros.index(3))

# Ao colocar . no final de um Tuple, ele te mostra os possíveis métodos que podem ser utilizados (count e index).
# Os métodos que começam com double underline são métodos mágicos.
