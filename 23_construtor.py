# Construtor
# É uma função (neste caso também método) chamada no momento que um objeto é criado.

# __init__ (initialize) é um método utilizado para contruir um objeto (construtor).
# Neste caso, as coordenadas x e y são construídas no momento que a classe Ponto é chamada.
# Os valores que serão atribuídos a x e y devem ser passados como argumentos na chamada da classe.
# Construtores simplificam muito o código no caso de criação de grande qtd de objetos do mesmo tipo.

class Ponto:                    # A classe Ponto define um novo tipo, que permite a criação de objetos.
    def __init__(self, x, y):    # __init__ (initialize) usa self para se referir ao objeto que está sendo criado.
        self.x = x              # Construção da coordenada x através do parâmetro x.
        self.y = y              # Construção da coordenada y através do parâmetro y.

    def move(self):             # move(self) é uma função (neste caso também método) dos objetos da classe Ponto.
        print("move")

    def desenha(self):          # desenha(self) é outra função (neste caso também método) dos objetos da classe Ponto.
        print("desenha")


ponto1 = Ponto(10, 20)          # Declarar argumentos na chamada da classe inicializa as coordenadas x e y do ponto1.
print(ponto1.x, ponto1.y)
ponto2 = Ponto(80, 30)          # Declarar argumentos na chamada da classe inicializa as coordenadas x e y do ponto2.
ponto2.x = 70
print(ponto2.x, ponto2.y)
