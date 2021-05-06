while True:
    try:

        entrada = int(input())
        if 0 <= entrada < 90 or entrada == 360:
            print('Bom Dia!!')
        elif 90 <= entrada < 180:
            print('Boa Tarde!!')
        elif 180 <= entrada < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
    except EOFError:
        break
