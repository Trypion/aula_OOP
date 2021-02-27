
notas = []

for i in range(3): 
  notas.append(float(input()))

soma = 0

peso1 = 2
peso2 = 3
peso3 = 5

notas[0] = notas[0]*peso1
notas[1] = notas[1]*peso2
notas[2] = notas[2]*peso3

for n in notas:
  soma += n

med = soma/(peso1 + peso2 + peso3)

print(f'MEDIA = {med}')