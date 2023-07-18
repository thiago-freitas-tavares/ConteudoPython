# Pacote (Package) - container para multiplos módulos.

# Botão direito na pasta do projeto HelloWorld + New + Python Package.
# Esse comando cria uma pasta com um __init__.py vazio, indicando que este diretório é um pacote.

# Botão direito na pasta do projeto HelloWorld + New + Directory
# Esse comando cria uma pasta vazia, neste caso a pasta é tratada como um diretório comum.

import modulos.utilidades                       # Importando o módulo.
modulos.utilidades.calc_frete()

from modulos.utilidades import calc_frete       # Importando as funções.
from modulos.utilidades import achar_max        # Forma de import que permite chamar as funções de maneira mais simples.
calc_frete()
print(achar_max([10, 30, 25, 7]))

from modulos import utilidades                  # Importando o pacote.
utilidades.calc_frete()

