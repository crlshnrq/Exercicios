colecao = []
unicos = 0

while True:
    try:
        entrada = input()
        if entrada not in colecao:
            colecao.append(entrada)

    except EOFError:
        print(len(colecao))
        break
