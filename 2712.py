import re


def dia(n):
    if n[7] == '1' or n[7] == '2':
        return 'MONDAY'
    elif n[7] == '3' or n[7] == '4':
        return 'TUESDAY'
    elif n[7] == '5' or n[7] == '6':
        return 'WEDNESDAY'
    elif n[7] == '7' or n[7] == '8':
        return 'THURSDAY'
    elif n[7] == '9' or n[7] == '0':
        return 'FRIDAY'


nCases = int(input())

for i in range(nCases):
    entrada = input()
    entradaRegex = re.compile(r"^[A-Z]{3}-[0-9]{4}$")
    entradaSearch = entradaRegex.match(entrada)
    if entradaSearch is None:
        print('FAILURE')
    else:
        print(dia(entrada))
