valores = []

for i in range(4):
  valores.append(int(input()))

repetidos = len(set(valores))

print(repetidos)
