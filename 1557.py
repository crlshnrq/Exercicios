# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15),
# correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.
#
# Entrada
# A carneiro consiste de vários inteiros, um valor por linha,
# correspondentes as ordens das matrizes a serem construídas.
# O final da carneiro é marcado por um valor de ordem igual a zero (0).
#
# Saída
# Para cada inteiro da carneiro imprima a matriz correspondente, de acordo com o exemplo.
# Os valores das matrizes devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço,
# onde T é igual ao número de dígitos do maior número da matriz. Após o último caractere de cada linha da matriz
# não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

multiplos = []
num = 1

for i in range(1, 30):
    multiplos.append(num)
    num *= 2

while True:

    N = int(input())
    if N == 0:
        pass
        break

    matriz = []

    for i in range(N):

        linha = []
        a = i
        for j in range(N):
            linha.append(multiplos[a])
            a+=1

        matriz.append(linha)

    temp = max(matriz)
    temp = len(str(max(temp)))

    for i in range(len(matriz)):

        for j in range(len(matriz)):
          print(str(matriz[i][j]).rjust(temp+1),end='')

        print('')
