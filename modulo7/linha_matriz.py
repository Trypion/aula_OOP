line_number = int(input().strip())
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

print(matrix[line_number])
if operation == "S":
  print(sum(matrix[line_number]))
else:
  print(sum(matrix[line_number])/12)
