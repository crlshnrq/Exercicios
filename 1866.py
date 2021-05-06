C = int(input())

lista = [1,-1]*500

for i in range(C):
    entrada = int(input())
    print(sum(lista[0:entrada]))
