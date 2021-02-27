comprimento = float(input())
largura = float(input())
gavetas = int(input())
tipo = input()

preco = 0

area = comprimento*largura

preco += area*100

if area > 2:
  preco += 50

if tipo == "mogno":
  preco += 150
elif tipo == "carvalho":
  preco += 125

preco += gavetas*30

if preco < 200:
  preco = 200

print(preco)

