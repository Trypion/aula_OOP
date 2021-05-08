import numpy as np
from numpy.lib.function_base import average

averages = []
for _ in range(12):
  row = [int(w) for w in input().strip().split(" ")]
  averages.append(round(np.average(row), 2))

print(*averages)