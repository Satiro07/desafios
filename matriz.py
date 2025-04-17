matriz = []
linhas = int(input('Quantidades de linhas: '))
colunas = int(input('Quantidade de colunas: '))
col = []
for i in range(0,colunas):
    col.append(0)
for i in range(0, linhas):
    matriz.append(col)
for i in matriz:
    print(i)

num = int(input('Diga um número: '))
pos_linha = int(input('Em qual linha deseja colocar o número? '))
pos_coluna = int(input('Coluna que deseja adicionar o número: '))

if matriz[pos_linha-1][pos_coluna-1] == 0:
    matriz[pos_linha-1][pos_coluna-1] = num

for i in matriz:
    print(i)
