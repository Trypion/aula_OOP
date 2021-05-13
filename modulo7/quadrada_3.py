import numpy as np

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
  
  line_length = len(str(matrix[size-1, size-1]))+1

  for row in matrix:
    response = ""
    count = 0
    for num in row:
      if count == 0:
        response += "".join("{:>{width}}".format(str(num), width=line_length-1))    
      else:
        response += "".join("{:>{width}}".format(str(num), width=line_length))
      count += 1
    response += '\r'
    print(response.rstrip())
    
  size = int(input())
  if(size != 0):
    print()