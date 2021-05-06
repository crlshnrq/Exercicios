O = str(input())
matriz = []
soma, compr =0,0

# Criando a matriz:
for j in range(0,12):
    linha = []
    for i in range(0,12):
        a = float(input())
        linha.append(a)
    matriz.append(linha)

for i in range(0,6):
    soma = soma + sum(matriz[i][12-i:12])
    # print((matriz[i][12-i:12]))
    compr = compr + len(matriz[i][12-i:12])

for i in range(6,12):
    soma = soma + sum(matriz[i][i+1:12])
    # print((matriz[i][i+1:12]))
    compr = compr + len(matriz[i][i+1:12])

if O =='S':
    print('{0:.1f}'.format(soma))
if O == 'M':
    print('{0:.1f}'.format(soma/compr))