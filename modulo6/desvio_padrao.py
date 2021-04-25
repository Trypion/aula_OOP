from statistics import stdev

quantidade = int(input())

lista = [float(input()) for _ in range(quantidade)]

print(stdev(lista))