num_cases = int(input())

for z in range(num_cases):
  rows, columns, punch_x, punch_y = [int(w) for w in input().strip().split(" ")]

  matrix = []

  for i in range(rows):
    matrix.append([int(w) for w in input().strip().split(" ")])

  for i in range(rows):
    for j in range(columns):
      distance_x = (10-abs(punch_x-1 - i)) if (10-abs(punch_x-1 - i)) >= 1 else 1
      distance_y = (10-abs(punch_y-1 - j)) if (10-abs(punch_y-1 - j)) >= 1 else 1
      matrix[i][j] += min(distance_x, distance_y)

  print(f"Parede {z+1}:")
  for row in matrix:
    print(" ".join([str(w) for w in row]))


