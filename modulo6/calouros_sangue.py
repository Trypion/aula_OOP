tam1 = int(input())

lista1 = []

for _ in range(tam1):
  lista1.append(input())

tam2 = int(input())
lista2 = []

for _ in range(tam2):
  lista2.append(input())

lista3 = []

for nome in lista2:
  if nome in lista1:
    lista3.append(nome)

proporcao = len(lista3)/len(lista1)

print(proporcao)