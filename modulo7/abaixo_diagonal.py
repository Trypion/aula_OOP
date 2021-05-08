operation = input().upper().strip()

element_count = 0
line = []
correct_line = []
matrix = []

for i in range(144):
  line.append(float(input().strip()))
  element_count += 1
  if element_count == 12:
    matrix.append(line)     
    element_count = 0
    line = []

line_sum = 0
column = 11
quantity = 0
for i in range(11, 0, -1):
  for j in range(column):
    line_sum += matrix[i][j]
    quantity += 1
  column -= 1

if operation == 'S':  
  print(round(line_sum, 1))
else:
  print(round((line_sum/quantity), 1))
