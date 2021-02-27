valor = float(input())

desc_padrao = valor*0.2
desc_500 = 0
desc_1000 = 0

if valor >= 500:
  desc_500 = valor*0.1

if valor >= 1000:
  desc_1000 = (valor-1000)*0.15

valor -= (desc_padrao + desc_500 + desc_1000)

print(valor)