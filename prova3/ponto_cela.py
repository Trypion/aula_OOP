rows, columns = [int(w) for w in input().strip().split(" ")]

matrix = []
for i in range(rows):
  matrix.append([int(w) for w in input().strip().split(" ")])

response = False

for i in range(rows):
  col_min = min(matrix[i])
  row = []
  for j in range(rows):
    row.append(matrix[j][matrix[i].index(col_min)])
  row_max = max(row)
  if col_min == row_max:
    response = (row.index(row_max)+1, matrix[i].index(col_min)+1)
    break

print(response)
