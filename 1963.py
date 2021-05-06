n = input().split()
n = list(map(float,n))

variacao = ((n[1]/n[0]) - 1)*100

print('{0:.2f}%'.format(variacao))

