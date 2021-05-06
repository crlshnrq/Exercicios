n = int(input())

carneiro = input().split()
carneiro = list(map(int, carneiro))

estrelas = 0
i = 0

while i >= 0 and i <= n:

    carneiro[i] -= 1
    if (carneiro[i] + 1) % 2 == 0:
        i -= 1
    else:
        i += 1
    estrelas += 1

print('{0} {1}'.format(estrelas,sum(carneiro)))

