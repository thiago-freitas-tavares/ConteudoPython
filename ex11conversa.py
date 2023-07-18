# Exercício 11 - Conversa


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def fala(self):
        print(f'Olá, {self.nome}!')


pessoa1 = Pessoa(input('Nome: '))       # Cada objeto é uma diferente instância da classe Pessoa.
pessoa1.fala()
pessoa2 = Pessoa(input('Nome: '))       # Cada objeto é uma diferente instância da classe Pessoa.
pessoa2.fala()
