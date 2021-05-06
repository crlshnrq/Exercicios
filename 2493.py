
def teste(ent, op):
    soma = ent[0] + ent[1] == ent[2]
    subtracao = ent[0] - ent[1] == ent[2]
    multiplicao = ent[0] * ent[1] == ent[2]

    if op == 'I' and soma is False and subtracao is False and multiplicao is False:
        return 'Acertou'
    elif op == '+' and soma is True:
        return "Acertou"
    elif op == '-' and subtracao is True:
        return "Acertou"
    elif op == '*' and multiplicao is True:
        return "Acertou"
    else:
        return "Errou"


while True:
    try:
        resultado = []
        n = int(input())
        lista = []
        palpites = {}
        # Montando os opçcoes
        for i in range(n):
            # separando as variaveis
            entrada = input().split()
            entrada.extend(entrada[1].split('='))
            entrada.remove(entrada[1])
            entrada = list(map(int, entrada))
            lista.append(entrada)
        # recebe os palpites:
        for j in range(n):
            participantes = input().split()
            nome = participantes[0]
            expressao = int(participantes[1])
            operador = participantes[2]
            palpites[nome] = teste(lista[expressao-1], operador)
        # confere quais palpites estão errados
        for i in palpites:
            if palpites[i] == 'Errou':
                resultado.append(i)
        if 1 <= len(resultado) < n:
            resultado = sorted(resultado)
            print(' '.join(resultado))
        elif len(resultado) >= n:
            print('None Shall Pass!')
        else:
            print('You Shall All Pass!')

    except EOFError:
        exit()
