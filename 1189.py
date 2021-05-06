
O = str(input())
matriz = []
soma, compr =0,0
contador = 1

# Criando a matriz:
for j in range(0,12):
    linha = []
    for i in range(0,12):
        a = float(input())
        linha.append(a)
    matriz.append(linha)

for i in range(0,6):
    soma = soma + sum(matriz[i][0:i])
    compr = compr + len(matriz[i][0:i])

for i in range(6,12):
    soma = soma + sum(matriz[i][0:i-contador])
    compr = compr + len(matriz[i][0:i-contador])
    contador += 2
    
if O =='S':
    print('{0:.1f}'.format(soma))
if O == 'M':
    print('{0:.1f}'.format(soma/compr))