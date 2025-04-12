robos = list()
quantidade_robos = int(input('Quantidade de robôs: '))
for i in range(0, quantidade_robos):
    sequencia = input('').strip()
    sequencia = list(map(int, sequencia.split()))
    robos.append(sequencia)
for i in robos:
    if i == i[::-1]:
        print('REBOLADO')
    else:
        print('NORMAL')
 