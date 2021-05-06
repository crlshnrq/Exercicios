import math

n = int(input())

minimo = n/math.log(n)

maximo = 1.25506*n/math.log(n)

print('{0:.1f} {1:.1f}'.format(minimo, maximo))
