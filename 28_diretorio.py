# Repositório (Directory - Pasta de Arquivos) e Arquivo (File).

# O módulo pathlib fornece classes com métodos que podem ser utilizados manipular repositório e arquivos.

from pathlib import Path

# Na chamada do módulo Path, o argumento pode ser um repositório ou arquivo.
# Se o argumento estiver vazio, a referência será o repositório atual.

# Absolute Path (caminho inicia no HD -> Exemplo c:\Program Files \Windows)
# Relative Path (caminho inicia no repositório atual)

caminho1 = Path('modulos')  # O objeto caminho1, do módulo Path, faz referência ao repositório modulos (python-content).
print(caminho1.exists())    # Devolve uma boolean confirmando ou não se o caminho existe.
# exemplo = Path('emails')  # Não existe repositório ou arquivo chamado emails.
# exemplo.mkdir()           # O método mkdir (make directory) cria o repositório emails.
# exemplo.rmdir()           # O método rmdir (remove directory) deleta o repositório emails.

caminho2 = Path()
# O argumento do método glob define o padrão da busca - '*'(all) ou '*.*'(all files) ou '*.extensão do arquivo').
print(caminho2.glob('*.py'))            # O método retorna um Generator Object. <generator object Path.glob at 0x000001C0B53DEAC0>.
for arquivo in caminho2.glob('*.py'):   # Podemos usar for ou while no gerador de objetos do método glob.
    print(arquivo)

"""
Generator Object: função que retorna um iterador, que produz uma sequência de
valores quando iterado. Útil quando se quer produzir uma grande sequência de
valores, mas sem armazenar todos na memória de uma vez.
"""