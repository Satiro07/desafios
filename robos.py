from random import randint
robos = list()
quantidade_robos = int(input('Quantidade de robôs: '))
for i in range(0, quantidade_robos):
    robo = []
    quantidade_digs = randint(1, 10)
    while quantidade_digs:
        digito = randint(1, 9)
        robo.append(digito)
    robos.append([robo])
print(robos)