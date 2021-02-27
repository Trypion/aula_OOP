notas = []
pesos = []

for i in range(3): 
  notas.append(float(input()))

for i in range(3):
  pesos.append(float(input()))

soma_notas = 0
soma_pesos = 0

for i in range(len(notas)):
  notas[i] *= pesos[i]

for n in notas:
  soma_notas += n

for n in pesos:
  soma_pesos += n

med = soma_notas/soma_pesos

if med >= 6:
  print(True)
else:
  print(False)