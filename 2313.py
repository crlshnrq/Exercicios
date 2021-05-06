
def tipo(lado_a, lado_b, lado_c):
    if lado_a == lado_b == lado_c:
        return 'Equilatero'
    elif lado_a == lado_b != lado_c or lado_b == lado_c != lado_a or lado_c == lado_a != lado_b:
        return 'Isoceles'
    else:
        return 'Escaleno'


def retangulo(lado_a, lado_b, lado_c):
    if (lado_a**2 == lado_b**2 + lado_c**2) or (lado_b**2 == lado_a**2 + lado_c**2) or \
            (lado_c**2 == lado_b**2 + lado_a**2):
        return 'S'
    else:
        return 'N'


entrada = list(map(int, input().split()))

a, b, c = entrada[0], entrada[1], entrada[2]

if (a < (b + c)) and (b < (a + c)) and (c < (b + a)):
    existencia = 'Valido'
    print('{0}-{1}'.format(existencia, tipo(a, b, c)))
    print('Retangulo: {}'.format(retangulo(a, b, c)))
else:
    existencia = 'Invalido'
    print(existencia)
