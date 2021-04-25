frase = list(input().replace(" ", "").lower())

repetidas = {letra:frase.count(letra) for letra in frase}

print(max(repetidas, key=repetidas.get))
