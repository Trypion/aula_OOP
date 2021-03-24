p, r = [int(w) for w in input().split()]

def calcula_saida(p, r):
  if p == 0:
    return "C"
  elif r == 0:
    return "B"
  else:
    return "A"

print(calcula_saida(p,r))
