entrada = float(input())

entrada = str(entrada)

if entrada == '-0.0':
    entrada = float(entrada)
    print('{0:.4E}'.format(entrada))
    exit()

entrada = float(entrada)
if entrada >= 0:
    print('+{0:.4E}'.format(entrada))
else:
    print('{0:.4E}'.format(entrada))