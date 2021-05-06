while True:
    N = int(input())
    if N == 0:
        break
    matriz = []
    #Cria matriz:
    for i in range(N):
        linha = []
        for j in range(N):
            a = 1
            linha.append(a)
        matriz.append(linha)
    #Substitui a matriz:
    origem = 1
    final = N-1
    a += 1
    while True:
        if origem >= final:
            break
        else:
            for i in range (origem,final):
                for j in range(origem,final):
                    matriz[i][j] = a
            origem += 1
            final -= 1
            a += 1
    #Imprime a matriz:
    for i in range(0,N):
        x = list(map(str,matriz[i]))
        print('  ',end='')
        print('   '.join(x))
    print('')