
robos = []
quant_robos = int(input('Quantidade de robôs: '))
for i in range(0, quant_robos):
    sequencia = input('Sequência: ')
    sequencia = list(map(int, sequencia.split()))
    robos.append(sequencia)
for robo in robos:
    cont = 1
    for i in range(0, len(robo)):
        if robo[i] < robo[cont]:
            pass
        else:
            print('NORMAL')

