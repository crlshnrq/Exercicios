n = int(input())
data = 0


def ano():
    global data
    data = int(input())
    # return data


def teste():
    global data
    data = 2015 - data
    if data <= 0:
        data = abs(data-1)
        print('{} A.C.'.format(data))
    else:
        print('{} D.C.'.format(data))


for i in range(n):
    ano()
    teste()
