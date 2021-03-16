x = input()

soma = 0
peso = len(x)
for i in range(len(x)-1):
  soma += int(x[i])*peso
  peso -=1

dv = 11 - soma %11
if dv >= 10:
  dv = 0

print(dv == int(x[-1]))