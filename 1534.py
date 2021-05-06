# Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.
#
# Entrada:
# A carneiro contém vários casos de teste e termina com EOF.
# Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70),
# que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.
#
# Saída:
# Para cada N lido, apresente a saída conforme o exemplo fornecido.

while True:
    try:
        N = int(input())
        origem = 0
        final = N-1
        matriz = []

        for j in range(N):
            linha = []
            for i in range(0,N):
                if i == final:
                    a = 2
                elif i == origem:
                    a = 1
                else:
                    a = 3
                linha.append(a)
            origem += 1
            final -= 1
            matriz.append(linha)


        for i in range(len(matriz)):
            print(*matriz[i],sep='')


    except EOFError:
        break