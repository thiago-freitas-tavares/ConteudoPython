# Lista 2D (listas dentro de lista)

matrix = [          # cada lista secundária representa um item da lista principal
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][2] = 0

for row in matrix:      # 0 in matrix = [1, 2, 3] -> row = [1, 2, 3]
    for item in row:    # 0 in row = 1 -> item = 1
        print(item)     #