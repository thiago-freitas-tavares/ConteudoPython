# Utilização de Classe para Definir Novos Tipos para Modelar Novos Conceitos.

# Tipos Básicos -> Números, Strings, Booleans.
# Tipos Complexos -> Lista, Tuple, Dicionário.

# Convenção de Nomeação Pascal
# classe    -> ConvencaoDeNomeacaoPascal
# função    -> convencao_de_nomeacao_pascal
# variáveis -> convencao_de_nomeacao_pascal

class Ponto:                # A classe Ponto define um novo tipo, que permite a criação de objetos.
    def move(self):         # move(self) é uma função (neste caso também método) dos objetos da classe Ponto.
        print("move")

    def desenha(self):      # desenha(self) é outra função (neste caso também método) dos objetos da classe Ponto.
        print("desenha")


ponto1 = Ponto()            # Cria objeto ponto1, que é do tipo Ponto.
ponto1.x = 10
ponto1.y = 20
print(ponto1.x, ponto1.y)
ponto1.desenha()            # Chama Método move ou Método desenha (Métodos com double underline são Métodos Mágicos).

ponto2 = Ponto()            # Cria objeto ponto2, do tipo Ponto. Cada objeto é uma diferente instância da classe Ponto.
ponto2.x = 80
ponto2.y = 30
print(ponto2.x, ponto2.y)
ponto2.move()
