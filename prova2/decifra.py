alfabeto = list("abcdefghijklmnopqrstuvwxyz")

permutado = list(input())
cifra = list(input())

decifrado = []
for letra in cifra:
  indice = permutado.index(letra)
  decifrado.append(alfabeto[indice])

print("".join(decifrado))
