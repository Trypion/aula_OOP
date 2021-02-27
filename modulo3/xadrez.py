import math

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

can_move = math.sqrt((x1 - x2)**2 + (y1-y2)**2) == math.sqrt(5)

print(can_move)