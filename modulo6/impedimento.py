num_atacantes, num_defensores = [int(w) for w in input().strip().split(' ')]
while(num_atacantes  != 0 and num_defensores != 0):
  atacantes = [int(w) for w in input().strip().split(' ')]
  defensores = [int(w) for w in input().strip().split(' ')]

  mais_perto = min(atacantes)

  count = 0

  for defensor in defensores:
    if defensor <= mais_perto:
      count += 1
      if count >= 2:
        break

  print("N" if count >= 2 else "Y")  
  num_atacantes, num_defensores = [int(w) for w in input().strip().split(' ')]
