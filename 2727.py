import re

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

while True:
    try:
        numCasos = int(input())
        for i in range(numCasos):
            codigo = input()
            codigoRegex = re.compile(r'[^\s]*')
            codigoCounter = codigoRegex.findall(codigo)
            numPontos = codigoCounter[0].count('.')
            contagemPontos = codigo.count('.')
            contagemEspacos = codigo.count(' ')
            if numPontos == 1:
                x = contagemPontos + 2 * contagemEspacos
                print(alfabeto[x-1])
            elif numPontos == 2:
                x = contagemPontos + 1 * contagemEspacos
                print(alfabeto[x-1])
            elif numPontos == 3:
                x = contagemPontos + 0 * contagemEspacos
                print(alfabeto[x-1])

    except EOFError:
        break
