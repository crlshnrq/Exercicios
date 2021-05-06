entrada = int(input())
resultado = ''

dicionario = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

if entrada >= 1000:
    entrada -= 1000
    resultado += dicionario[1000]

while entrada >= 100:
    if entrada >= 900:
        entrada -= 900
        resultado += dicionario[900]
    elif entrada >= 500:
        entrada -= 500
        resultado += dicionario[500]
    elif entrada >= 400:
        entrada -= 400
        resultado += dicionario[400]
    else:
        entrada -= 100
        resultado += dicionario[100]

while entrada >= 10:
    if entrada >= 90:
        entrada -= 90
        resultado += dicionario[90]
    elif entrada >= 50:
        entrada -= 50
        resultado += dicionario[50]
    elif entrada >= 40:
        entrada -= 40
        resultado += dicionario[40]
    else:
        entrada -= 10
        resultado += dicionario[10]

while entrada > 0:
    if entrada >= 9:
        entrada -= 9
        resultado += dicionario[9]
    elif entrada >= 5:
        entrada -= 5
        resultado += dicionario[5]
    elif entrada >= 4:
        entrada -= 4
        resultado += dicionario[4]
    elif entrada >= 1:
        entrada -= 1
        resultado += dicionario[1]
print(resultado)
