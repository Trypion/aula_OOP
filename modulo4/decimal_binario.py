numero = int(input())

binario = []

if numero == 0:
  print(0)

while numero != 0:
  binario.append(numero%2)
  numero = int(numero/2)

binario.reverse()

for i in binario:
  print(i, end="")

# como alteranativa da pra fazer
# print(bin(numero)[2:])
