while True:

  N = int(input())
  if N == 0:
    break

  matriz = []
  counter = True
  for i in range(1,N+1):

    linha = []

    a = i
    counter = True

    for j in range(N):

      linha.append(a)

      if a == 1:
        counter = False

      if counter == False:
        a += 1

      if counter == True:
        a -= 1

    matriz.append(linha)

  # for i in range(0,N):
  #   x = list(map(str,matriz[i]))
  #   print('  ',end='')
  #   print('   '.join(x))
  #   print('')

  for i in range(len(matriz)):
    print('  ',end='')
    print(*matriz[i],sep='   ')
