# Operadores de Loop Aninhados (Nested Loop)

for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")

f = [5, 2, 5, 2, 2]
for i in f:
    print("*" * i)              # letra F

f = [1, 1, 1, 1, 5]
for a in f:                     # 0 in f = 1 -> a = 1 | # 1 in f = 1 -> a = 1 |...| # 4 in f = 5 -> a = 5 | # 5 in f = X
    saida = ""                  # saida setada em "vazio"
    for b in range(a):          # 0 in range(1) = 0 -> b = 0 | # 1 in range(1) = X |...| # 0 in range(5)...5 in range(5) = X
        saida = saida + "*"     # letra L
    print(saida)
