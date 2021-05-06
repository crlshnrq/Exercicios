N = int (input())
T = input().split()
T = list(map(int,T))

minimo = min(T)
minimo = T.index(minimo)

print(minimo+1)