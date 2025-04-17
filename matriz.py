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

print()
print('Matriz transposta:')

c = 0
for i in matriz:
    for x in i:
        c += 1
    break
mt = []
for x in range(0, c):
    mt1 = []
    cont = 0
    for y in matriz:
        mt1.append(matriz[cont][x])
        cont += 1
    mt.append(mt1)
for i in mt:
    print(i)
    