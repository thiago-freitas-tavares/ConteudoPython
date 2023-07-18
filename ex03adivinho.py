# Exercício 3 - Jogo de Adivinhação

x = 9
n = 0
while n != x:
    n = int(input("Palpite: "))
print("Até que enfim.")

numero_secreto = 9
qtd_palpite = 0
qtd_max_palpite = 5
while qtd_palpite < qtd_max_palpite:
    palpite = int(input("Palpite: "))
    qtd_palpite += 1
    if palpite == numero_secreto:
        print("Até que enfim.")
        break
else:
    print("Você perdeu.")