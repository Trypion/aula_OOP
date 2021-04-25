tam = int(input())
count = 0

while(tam != 0):
  count += 1
  lista = [int(w) for w in input().split(' ')]
  for i in range(tam):
    if i+1 == lista[i]:
      ganhador = lista[i]
      break
  print(f'\nTeste {count}\n{ganhador}')
  tam = int(input())
  