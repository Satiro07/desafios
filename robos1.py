
robos = []
quant_robos = int(input('Quantidade de robôs: '))
for i in range(0, quant_robos):
    sequencia = input('Sequência: ')
    sequencia = list(map(int, sequencia.split()))
    robos.append(sequencia)
for robo in robos:
    cont = 1
    verdade = False
    if robo[0] < robo[cont]:
        for i in range(1, len(robo)-1):
            cont += 1
            if robo[-2] < robo[-1]:
                verdade = False
                break
            if robo[i] < robo[cont]:
                verdade = True
            elif robo[i] == robo[cont]:
                verdade = False
                break
            
            else:
                verdade = True
    if verdade == True:
        print('Certo')
    else:
        print('NORMAL')

