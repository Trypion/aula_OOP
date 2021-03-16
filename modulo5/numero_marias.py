tam = int(input())

count = 0
for _ in range(tam):
  nome = input()
  lista = nome.split()

  for item in lista:
    if item.lower() == 'maria':
      count += 1

print(count)
