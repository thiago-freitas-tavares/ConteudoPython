# Módulo -> um arquivo.py com código Python

# Dependendo da complexidade de uma aplicação, por questão de organização, ao invés de escrever o código inteiro
# dentro do mesmo arquivo.py, podemos fragmentar o código em múltiplos arquivos.py, que chamamos de módulos.
# É possível importar um módulo dentro de outro módulo.

from modulos import conversor

print(conversor.lbs_to_kg(200))
print(conversor.kg_to_lbs(100))

# Ao invés de importar um módulo inteiro, podemos importar funções específicas deste módulo.

from modulos.conversor import kg_to_lbs     # Com o cursor um espaço após o import, clique Ctrl+Espaço para ver a
from modulos.conversor import lbs_to_kg     # lista completa de funções definidas neste módulo.

print(lbs_to_kg(200))               # Importando esta função específica, a chamada da função fica mais resumida.
print(kg_to_lbs(100))

# À medida com que os códigos vão ficando mais complexos, vai ficando cada vez mais importante a organização
# do código em funções, classes e módulos.
