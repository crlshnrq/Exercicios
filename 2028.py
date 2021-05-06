x = 1
while True:

    try:

        N = int(input())
        lista = []
        lista.extend([0])

        for i in range(1, N + 1):
            temp = [i]*i
            lista.extend(temp)

        lista = list(map(str,lista))

        if len(lista) <= 1:
            print('Caso {0}: {1} numero'.format(x, len(lista)))
        else:
            print('Caso {0}: {1} numeros'.format(x, len(lista)))
        print(' '.join(lista) + '\n')

        x += 1


    except EOFError:
        break
