while True:
  try:
    rows, columns = [int(w) for w in input().strip().split(" ")]

    matrix = []

    for _ in range(rows):
      matrix.append([int(w) * 9 for w in input().strip().split(" ")])

    for i in range(rows):
      for j in range(columns):
        if matrix[i][j] == 0:  
          for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < rows and 0 <= nj < columns and matrix[ni][nj] == 9:
              matrix[i][j] += 1
             
    for row in matrix:
      print("".join([str(w) for w in row]))

  except EOFError:
    break
