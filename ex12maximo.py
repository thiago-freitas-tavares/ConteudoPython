# Exercício 12 - Maior Número de uma Lista
# Criar uma função (achar_max) que deve receber uma lista de números e retornar o de maior valor.
# Colocar esta função (achar_max) em um módulo separado (utilidades) e chamá-la neste módulo (ex12maximo).

from modulos.utilidades import achar_max

numeros = [25, 4, 54, 34, 78, 16]

# Se trocassemos as linhas 12 e 13 de lugar, a chamada do max(numeros) padrão do Python não funcionaria mais.
# o max da linha 12 está roxo, pois se refere a uma função built-in do Python.

print(max(numeros))
max = achar_max(numeros)

# Como substituímos o max padrão por achar_max, dessa linha para baixo não existe mais max padrão (roxo).

print(max)

# A variável max fica sublinhada em amarelo (Shadows built-in name),
# pois por padrão existe uma função max da linguagem Python, que faz exatamente o que nossa função achar_max faz.
# Neste caso, estaríamos sobrescrevendo a função padrão (o que não é interessante).
