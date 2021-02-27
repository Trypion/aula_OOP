import math

valor = float(input())
parcelas = int(input())
taxa = float(input())/100

montante = valor * math.pow((1+taxa), parcelas)

print(round(montante, 2))