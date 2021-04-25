lista1 = [int(w) for w in input().strip().split(' ')]
lista2 = [int(w) for w in input().strip().split(' ')]

compativel = 'Y'
for i in range(len(lista1)):
  if lista1[i] == lista2[i]:
    compativel = 'N'
    break

print(compativel)