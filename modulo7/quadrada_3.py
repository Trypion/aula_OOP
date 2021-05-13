import numpy as np
from numpy.core.fromnumeric import reshape
size = int(input())
while (size != 0): 

  matrix = []
  row = []
  count = 1
  for _ in range(size): 
    row.append(count)
    count = count*2

  row = np.array(row)
  count = 1
  for _ in range(size):
    matrix.append(row*count)
    count = count*2    

  matrix = np.array(matrix) 
  
  for row in matrix:
    response = ""
    count = 0
    for num in row:
      column_length = len(str(matrix[count, size-1]))+1
      response += "".join("{:>{width}}".format(str(num), width=column_length))
      count += 1    
    print(response)

  size = int(input())
  if(size!=0):
    print()
  