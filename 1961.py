entrada_1 = input().split()

entrada_2 = input().split()

entrada_2 = list(map(int, entrada_2))

P, N = int(entrada_1[0]), int(entrada_1[1])

game = True

for i in range(len(entrada_2)-1):
    if abs(entrada_2[i] - entrada_2[i+1]) > P:
        print('GAME OVER')
        game = False
        break

if game is True:
    print('YOU WIN')
