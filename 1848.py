grito = []

num = 0



while True:

    entrada = input()

    if entrada == 'caw caw':
        grito.append(entrada)
        print(num)
        num = 0
    if entrada == '---':
        num += 0
    if entrada == '--*':
        num += 1
    if entrada == '-*-':
        num += 2
    if entrada == '-**':
        num += 3
    if entrada == '*--':
        num += 4
    if entrada == '*-*':
        num += 5
    if entrada == '**-':
        num += 6
    if entrada == '***':
        num += 7

    if len(grito) == 3:
        break

