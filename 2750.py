def tracos_hor(x):
    print('-' * x)


def titulos():
    print('|' + ' ' * 2 + 'decimal' + ' ' * 2, end='')
    print('|' + ' ' * 2 + 'octal' + ' ' * 2, end='')
    print('|' + ' ' * 2 + 'Hexadecimal' + ' '*2 + '|')


def dados(vezes, elementos):
    for i in range(vezes):
        deci = elementos['decimal'][i]
        octa = elementos['octal'][i]
        hexa = elementos['Hexadecimal'][i]
        print('|' + ' ' * (10 - 3 - len(deci)) + deci + ' ' * 4, end='')
        print('|' + ' ' * (8 - 3 - len(octa)) + octa + ' ' * 4, end='')
        print('|' + ' ' * (15 - 7 - len(hexa)) + hexa + ' ' * 7 + '|')


tabela = {'decimal': ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'),
          'octal': ('0', '1', '2', '3', '4', '5', '6', '7', '10', '11', '12', '13', '14', '15', '16', '17'),
          'Hexadecimal': ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')}

numHori = 39  # Numero de traços horizontais
numVert = 16  # Numero de tracos verticais (linhas)
numEspVert = numHori - 2
tracos_hor(numHori)
titulos()
tracos_hor(numHori)
dados(numVert, tabela)
tracos_hor(numHori)
