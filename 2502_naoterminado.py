
def descript(cripto1, cripto2, text):
    for x in range(len(text)):
        for y in range(len(cripto1)):
            if x == 0 and text[x] == cripto1[y].upper():
                text[x] = cripto2[y].upper()
                break
            elif text[x] == cripto1[y]:
                text[x] = cripto2[y]
                break

    return ''.join(text)


while True:
    try:
        entrada = input().split()
        C = int(entrada[0])
        n = int(entrada[1])

        entrada_1 = input().lower()
        entrada_2 = input().lower()
        criptografia_1 = entrada_1 + entrada_2
        criptografia_2 = entrada_2 + entrada_1

        for i in range(n):
            texto = list(input())
            criptografado = descript(criptografia_1, criptografia_2, texto)
            print(criptografado)
        

    except EOFError:
        break
