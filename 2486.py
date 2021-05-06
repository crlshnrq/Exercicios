entrada = int(input())

tabela = {'suco de laranja': 120,
          'morango fresco': 85,
          'mamao': 85,
          'goiaba vermelha': 70,
          'manga': 56,
          'laranja': 50,
          'brocolis': 34}

while entrada != 0:

    calorias = 0
    for i in range(entrada):

        alimentos = input().split()
        numero = int(alimentos[0])
        tipo = ' '.join(alimentos[1:])

        calorias += numero * tabela[tipo]

    if 110 <= calorias <= 130:
        print("{} mg".format(calorias))
    elif calorias <= 110:
        print('Mais {} mg'.format(110 - calorias))
    else:
        print('Menos {} mg'.format(calorias - 130))

    entrada = int(input())
