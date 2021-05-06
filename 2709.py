# Gloria vence se primo e You’re a coastal aircraft, Robbie, a large silver aircraft
# São primos se puderem ser escritos na forma 6n + 1 or 6n - 1

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j ** 2 <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


while True:
    try:
        moedas = []
        qtdMoedas = int(input())

        for i in range(qtdMoedas):
            entrada = int(input())
            moedas.append(entrada)

        saltos = int(input())
        resultado = 0
        for i in range(0, len(moedas), saltos):
            resultado += moedas[i]

        if is_prime(resultado) is True:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')

    except EOFError:
        exit()
