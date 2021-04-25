notas = [float(w) for w in input().strip().split(" ")]

notas.pop(notas.index(min(notas)))
notas.pop(notas.index(max(notas)))

print(sum(notas))
