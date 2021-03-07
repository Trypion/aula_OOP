numero = int(input())

valores = []

if numero == 1:
  regular = False
else:
  regular = True

while numero != 1:
  if numero%2 == 0:
    numero = numero/2
    valores.append(2) 
  elif numero%3 == 0:
    numero = numero/3
    valores.append(3)
  elif numero%5 == 0:
    numero = numero/5
    valores.append(3)
  else:    
    numero = numero/numero
    valores.append(numero)

for i in valores:
  if i not in [2, 3, 5]:
    regular = False

print(regular)
