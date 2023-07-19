# Inheritage (Herança) -> Mecanismo de reutilização de código.

# DRY - Don't Repeat Yourself - uma forma de simplificar o código.

# 1. Exemplo com Utilização de Herança


class Mamifero:
    def andar(self):
        print('Ande')


class Cachorro(Mamifero):       # classe Cachorro herda todos os métodos definidos na classe principal Mamífero.
    def latir(self):
        print('Lata!')


class Gato(Mamifero):           # classe Gato herda todos os métodos definidos na classe principal Mamífero.
    pass                        # Python não aceita classe vazia, neste caso, declarar pass.


cachorro1 = Cachorro()
cachorro1.andar()
cachorro1.latir()
gato1 = Gato()
gato1.andar()

# 2. Exemplo sem Utilização de Herança


class Dog:
    def __init__(self, name):
        self.name = name

    def andar(self):                        # Nunca defina a mesma função mais de uma vez
        print(f'Ande, {self.name}!')


class Cat:
    def __init__(self, name):
        self.name = name

    def andar(self):                        # Nunca defina a mesma função mais de uma vez
        print(f'Ande, {self.name}!')


dog1 = Dog(input('Dog: '))
dog1.andar()
cat1 = Cat(input('Cat: '))
cat1.andar()
