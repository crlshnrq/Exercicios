entrada = input().split()
entrada = list(map(int,entrada))
b = 0

for i in range(len(entrada)):

    a = 0
    duple = entrada.copy()

    duple.remove(duple[i])

    for j in duple:
        if j < sum(duple) - j:
            a += 1

    if a == 3:
        print('S')
        break
    else:
        b += 1

if b == 4:
    print('N')