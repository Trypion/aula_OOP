from statistics import geometric_mean

quantidade = int(input())

lista = [float(input()) for _ in range(quantidade)]

print(geometric_mean(lista))