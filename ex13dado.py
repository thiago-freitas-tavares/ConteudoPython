# Exercício 13 - Lances de Dados

import random


class Dados:
    def roll(self):
        primeiro = random.randint(1, 6)
        segundo = random.randint(1, 6)      # Para retornar uma lista -> return [primeiro, segundo].
        return primeiro, segundo            # Dessa forma o return entende que se trata de um tuple.


lance = Dados()                             # Tem que criar um objeto da classe Dados para poder usar seus métodos.
print(lance.roll())
