while True:
    try:

        entrada = float(input())
        #Convertendo de graus para tempo:
        tempo = entrada * 240
        segundos = int(tempo % 60)
        tempo = int(tempo / 60)
        minutos = tempo % 60
        horas = int(tempo / 60) + 6
        if horas >= 24:
            horas -= 24

        if 0 <= entrada < 90 or entrada == 360:
            print('Bom Dia!!')
        elif 90 <= entrada < 180:
            print('Boa Tarde!!')
        elif 180 <= entrada < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")

        print('{0:02d}:{1:02d}:{2:02d}'.format(horas, minutos, segundos))
    except EOFError:
        break
