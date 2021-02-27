a, b = [int(i) for i in input().split()]

resto = max(a, b)%min(a, b)

if resto == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
