# Read an uppercase character that indicates an operation that will be performed in an array M[12][12].
# Then, calculate and print the sum or average considering only that numbers that are above the main diagonal of the array,
# like shown in the following figure (green area).

# Input
# The first line of the input contains a single uppercase character O ('S' or 'M'),
# indicating the operation Sum or Average (Média in portuguese) to be performed with the elements of the array.
# Follow 144 floating-point numbers of the array.

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

for i in range(0,5):
    soma = soma + sum(matriz[i][i+1:11-i])
    print(matriz[i][i+1:11-i])
    compr = compr + len(matriz[i][i+1:11-i])

if O =='S':
    print('{0:.1f}'.format(soma))
if O == 'M':
    print('{0:.1f}'.format(soma/compr))