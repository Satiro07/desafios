matriz = []
linhas = int(input('Quantidades de linhas: '))
colunas = int(input('Quantidade de colunas: '))

for i in range(0,linhas):
    col = []
    for y in range(0, colunas):
        add_col = int(input(f'Número na linha {i+1} e coluna {y+1}: '))
        col.append(add_col)
    matriz.append(col)

for i in matriz:
    print(i)
