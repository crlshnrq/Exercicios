import re


def separador(elemento):  # Separa os elementos
    elementoregex = re.compile(r'[A-Z]{1}[a-z]?\d*')
    elementofindall = elementoregex.findall(elemento)
    return elementofindall


casos = int(input())  # Numero de casos totais:

for j in range(casos):  # Numero de formulas perigosas:

    numIndex = int(input())
    elIndex = []

    for i in range(numIndex):  # Recebe os elementos perigosos
        el = input()
        elementoSeparado = separador(el)
        elIndex.append(elementoSeparado)

    numTestes = int(input())  # Numero de elementos a serem testados

    for i in range(numTestes): # Recebe os elementos a serem testados

        elTeste = input()
        testeSeparado = separador(elTeste)
        check = False

        for h in range(len(elIndex)):
            if elIndex[h][0] in testeSeparado:  # Confere se o inicio do elemento base esta no elemento testado
                x = testeSeparado.index(elIndex[h][0])
                c = len(elIndex[h])
                y = ''.join(testeSeparado[x:c + x])

                if ''.join(elIndex[h]) == y:
                    check = True

        if check is True:
            print('Abortar')
        else:
            print('Prossiga')

    if j < casos-1:
        print('')
