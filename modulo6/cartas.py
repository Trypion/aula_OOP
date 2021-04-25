lista = [int(w) for w in input().strip().split(' ')]

if all(lista[i] < lista[i+1] for i in range(len(lista)-1)):
  print('C')
elif all(lista[i] > lista[i+1] for i in range(len(lista)-1)):
  print('D')
else:
  print('N')