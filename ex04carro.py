# Exercício 4 - Jogo do Carro

comando = ""
anterior = "PARE"   # Poderia utilizar uma variável booleana também
# while comando != "FIM": Da para substituir por True, neste caso, o while vai rodar até chegar em um break.
while True:
    comando = input("> ").upper()
    if comando == "MENU":
        print("GO   - iniciar o carro\nPARE - parar o carro\nFIM  - sair")
    elif comando == "GO" and anterior != "GO":
        print("Carro iniciado... Pronto para partida.")
        anterior = comando
    elif comando == "GO" and anterior == "GO":
        print("O carro já encontra-se ligado.")
    elif comando == "PARE" and anterior != "PARE":
        print("Carro parado.")
        anterior = comando
    elif comando == "PARE" and anterior == "PARE":
        print("O carro já encontra-se parado.")
    elif comando == "FIM":
        print("Fim.")
        break
    else:
        print("Não compreendo.")

"""
comando = input("> ").lower()
while comando != "menu":
    print("Não compreendo.")
    comando = input("> ").lower()
else:
    print("GO   - iniciar o carro\nPARE - parar o carro\nFIM  - sair")
    comando = input("> ").upper()
while comando != "GO" and comando != "PARE" and comando != "FIM":
    print("Não compreendo.")
    comando = input("> ").upper()
    if comando == "GO":
        print("Carro iniciado... Pronto para partida.")
    elif comando == "PARE":
        print("Carro parado.")
    elif comando == "FIM":
        print("Fim.")
"""
