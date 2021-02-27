import math
import decimal

x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(i) for i in input().split()]

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(round(decimal.Decimal(distancia), 4))