QT = int(input())

for i in range(QT):
    entrada = input().split()
    players = {
        entrada[1]: entrada[0],
        entrada[3]: entrada[2]
    }
    num = input().split()
    num = list(map(int,num))
    soma = sum(num)
    if soma % 2 == 0:
        print(players['PAR'])
    else:
        print(players['IMPAR'])