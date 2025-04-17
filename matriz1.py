m = [[1,2], [3,4],[5,6]]
for i in m:
    print(i)
print()
print('Matriz transposta:')

mt = []
c = 0
for i in m:
    for x in i:
        c += 1

for x in range(0, c):
    mt1 = []
    cont = 0
    for y in m:
        mt1.append(m[cont][x])
        cont += 1
    mt.append(mt1)
for i in mt:
    print(i)
    
    
