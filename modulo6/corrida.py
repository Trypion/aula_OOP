carros, voltas  = [int(w) for w in input().strip().split(" ")]

tempos = []
for _ in range(carros):
  tempos.append(sum([int(w) for w in input().split(" ")]))

print(tempos.index(min(tempos))+1)
print(tempos.index(sorted(tempos)[1])+1)
print(tempos.index(sorted(tempos)[2])+1)
