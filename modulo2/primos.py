import math
from decimal import Decimal

n = int(input())

menor = n/math.log(n)

maior = 1.25506*menor

print(round(Decimal(menor), 1), round(Decimal(maior), 1))
