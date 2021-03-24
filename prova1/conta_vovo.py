dias, saldo = [int(w) for w in input().split()]

menor = saldo
for _ in range(dias):
  saldo += int(input())
  if saldo < menor:
    menor = saldo

print(menor)