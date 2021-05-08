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
quantity = 0
start = 1
end = 11
for i in range(5):
  for j in range(start, end):
    line_sum += matrix[i][j]
    quantity += 1
  end -= 1
  start += 1

if operation == 'S':  
  print(round(line_sum, 1))
else:
  print(round((line_sum/quantity), 1))
