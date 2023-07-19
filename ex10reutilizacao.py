# Exercício 10 - Funções Reutilizáveis
# Via de regra, o input e o print(output) ficam de fora das funções, pois podem variar de caso em caso.


def conversor_emote(mensagem):
    palavras = mensagem.split(' ')  # quebra a string em uma lista com as palavras separadas.
    print(palavras)
    emote = {
        ":)": "🙂",
        ":(": "😔",
        "(:": "🙃"
    }
    saida = ""
    for palavra in palavras:
        saida += emote.get(palavra, palavra) + " "  # A função .get() procura o 1o item do argumento no dicionário
    return saida                                    # Se não encontrar, devolve o 2o item do argumento como resultado


print(conversor_emote(input("> ")))
