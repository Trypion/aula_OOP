rows, columns = [int(w) for w in input().strip().split(" ")]

start_x, start_y = [int(w) for w in input().strip().split(" ")]

matrix = []
for _ in range(rows):
    matrix.append([int(w) for w in input().strip().split(" ")])


response = ()

start_x -= 1
start_y -= 1
previous_x = -1
previous_y = -1
while (not response):
  count = 0
  for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    ni = start_x + di
    nj = start_y + dj
    if 0 <= ni < rows and 0 <= nj < columns and matrix[ni][nj] == 1 and (ni, nj) != (previous_x, previous_y):
      count = 0
      previous_x = start_x
      previous_y = start_y
      start_x = ni
      start_y = nj
    else:
      count += 1
  if count == 4:
    response = (start_x+1, start_y+1)

print(" ".join(response))
