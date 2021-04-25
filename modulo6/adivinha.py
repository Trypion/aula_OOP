tam = int(input())

for _ in range(tam):
  sl, numero = [int(w) for w in input().split(' ')]

  palpites = [int(w) for w in input().split(' ')]

  vencedor = min(range(len(palpites)), key=lambda x: abs(palpites[x]-numero))

  print(vencedor+1)