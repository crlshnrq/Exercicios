while True:
    try:
        # recebe o numero de casos:
        numTrab = int(input())
        # recebe a dificuldade dos trabalhos:
        difTrab = list(map(int, input().split()))
        rangel = 0
        contador = 0
        atual
        anterior
        while True:
            for i in difTrab:
                if rangel + i <= sum(difTrab) - i:
                    rangel += i
                    difTrab.remove(i)
            contador += 1

        print(abs(rangel-sum(difTrab)))

    except EOFError:
        break
