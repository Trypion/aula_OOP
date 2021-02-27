dias = int(input())
km = int(input())

valor = 0

valor += dias*45
if km/dias >= 60 :
  valor += (km-60*dias)*0.5

print(valor)