# Dicionário

# Os pares abaixo (variável e atribuições) são conhecidos como key-value pairs (chaves e valores).

# Nome: Thiago Tavares
# Email: tfreitast88@gmail.com
# Telefone: 914842572
# Endereço: Rua 3750

# Um Dicionário armazena key-value pairs.

cliente = {
    "Nome": "Thiago Tavares",
    "Email": "tfreitast88@gmail.com",
    "Telefone": 914842572,
    "Endereço": True
}

cliente["Nome"] = "Thiago Freitas Tavares"
print(cliente["Nome"])                              # Case sensitive.
print(cliente["Email"])
print(cliente.get("Aniversario"))                   # Método .get resulta none, caso a chave não exista. Sem o Método .get da erro.
print(cliente.get("Aniversário", "19/06/1988"))     # Da para incluir dado em chave que não existe.
cliente["Aniversario"] = "01/11/1955"
print(cliente.get("Aniversario"))
