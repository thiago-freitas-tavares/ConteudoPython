# Standard Library Python - biblioteca padrão de módulos python

# Caminho: External Libraries -> Python 3.11 (NomeDoProjeto) -> Lib (no PyCharm)
# Google python 3 module index -> Link Python Documentation (lista de todos os módulos com explicação).

import random

for i in range(3):
    print(random.random())          # A função random retorna um valor aleatório entre 0 e 1.
    print(random.randint(0, 10))    # A função randint retorna um valor aleatório dentro do argumento declarado.

membros = ['Xis', 'Letty', 'Briny', 'Paris', 'Milta']
lider = random.choice(membros)
print(lider)
