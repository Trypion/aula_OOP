bandeijas = int(input())

quebrados = 0

for n in range(bandeijas):
  latas, copos = [int(i) for i in input().split()]
  if latas > copos:
    quebrados += copos

print(quebrados)
