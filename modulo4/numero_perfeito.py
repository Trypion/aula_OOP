quantidade = int(input())

def verifica_perfeito(x):
  divisores = []
  for i in range(1, x):
    if x%i == 0:
      divisores.append(i)

  soma_divisores = sum(divisores)
  if soma_divisores == x:
    return True
  else:
    return False

for i in range(quantidade):  
  numero = int(input())
  if verifica_perfeito(numero):
    print(f"{numero} eh perfeito")
  else:
    print(f"{numero} nao eh perfeito")