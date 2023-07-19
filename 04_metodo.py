# Funções de String (Objeto) - Chamadas Métodos

curso = 'python para iniciantes'    # curso é uma variável, mas quando recebe string, vira um objeto.
print(curso.title())

# Uma string em Python é tratada como um objeto
# As funções upper(), lower(), find(), replace() não modificam a string original, criam novas.
# Quando uma função faz parte de um objeto, ela é chamada de método (curso.upper()).
# print() e input() são exemplos de funções gerais.

print(curso[0])
print(curso[-1])
print(curso[0:3])   # não pega o último valor
print(curso[3:])
print(curso[:15])
print(curso[:])
print(len(curso))   # função lenght
print(curso.upper())
print(curso.lower())
print(curso.find('t'))
# Case sensitive
print(curso.replace('para', '4'))
print('Python' in curso)
# Strings em Python são imutáveis.
print(curso)
