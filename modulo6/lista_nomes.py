tam1 = int(input())
lista1 = []

for _ in range(tam1):
  lista1.append(input())

tam2 = int(input())
lista2 = []

for _ in range(tam2):
  lista2.append(input())

lista1 += lista2

lista1.sort()

print("\n".join(lista1))
