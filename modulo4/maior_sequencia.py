tam = int(input())

valores = []

for i in range(tam):
  valores.append(int(input()))

maior = max(valores)

posicao = valores.index(maior)

print(maior, posicao+1)