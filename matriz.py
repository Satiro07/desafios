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
pos_linha = int(input('Em qual linha deseja colocar o número? '))-1
pos_coluna = int(input('Coluna que deseja adicionar o número: '))-1

matriz[pos_linha][pos_coluna] = num
for i in matriz:
    print(i)