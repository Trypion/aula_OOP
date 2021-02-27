import math

nota = float(input())

if nota*10%10 < 2.5:
  print(math.floor(nota))
elif 2.5 <= nota*10%10 < 7.5:
  print(math.floor(nota)+0.5)  
else:
  print(math.ceil(nota))
