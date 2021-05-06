
entrada = int(input())


def conversao(nota):
    if nota == 0:
        return 'E'
    elif 1 <= nota <= 35:
        return "D"
    elif 36 <= nota <= 60:
        return "C"
    elif 61 <= nota <= 85:
        return "B"
    elif 85 <= nota <= 100:
        return "A"


print(conversao(entrada))
