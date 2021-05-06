testes = int(input())


def eye(op, r, g, b):
    cores = [r, g, b]
    if op == 'max':
        return max(cores)
    if op == "min":
        return min(cores)
    if op == "mean":
        return sum(cores)/len(cores)
    if op == "eye":
        return 0.3 * r + 0.59 * g + 0.11 * b


for i in range(testes):
    operacao = input()
    red, green, blue = ([int(x) for x in input().split()])
    x = eye(operacao, red, green, blue)
    print("Caso #{0}: {1}".format(i+1, int(x)))
