consumo = int(input())

custo = 0.0

for i in range(1, 31 if consumo>=30 else consumo+1):
  custo += 0.09556

if consumo > 30:
  for i in range(31, 101 if consumo>=100 else consumo+1):
    custo += 0.16698

if consumo > 100:
  for i in range(101, 201 if consumo >= 200 else consumo+1):
    custo += 0.25052

if consumo > 200:
  for i in range(201, consumo+1):
    custo += 0.27836

print(round(custo, 2))