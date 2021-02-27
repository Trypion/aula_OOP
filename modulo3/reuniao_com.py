niver1 = int(input())
niver2 = int(input())
niver3 = int(input())

niver_count = 3

if niver1 == niver2 == niver3:
  niver_count = 1
elif niver1 == niver2 or niver2 == niver3 or niver1 == niver3:
  niver_count = 2

print(niver_count)