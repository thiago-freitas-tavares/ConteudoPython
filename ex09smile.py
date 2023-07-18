# Exercício 9 - Lista de Emoticon em Dicionário

mensagem = input("> ")
palavras = mensagem.split(' ')  # quebrar a string em uma lista com as palavras separadas
print(palavras)
emote = {
    ":)": "🙂",
    ":(": "😔",
    "(:": "🙃"
}
saida = ""
for palavra in palavras:
    saida += emote.get(palavra, palavra) + " "  # A função .get() procura o primeiro item do argumento no dicionário
print(saida)                                    # Se não encontrar, devolve o segundo item do argumento como resultado
