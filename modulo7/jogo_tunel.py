while(True):
  try:
    rows, columns = [int(w) for w in input().strip().split(" ")]

    matrix = []
    for _ in range(rows):
        matrix.append([w for w in input().strip().split(" ")])


    for i in range(rows):
      for j in range(columns):
        if matrix[i][j] == 'X':
          start_x = i
          start_y = j

    previous_x = -1
    previous_y = -1

    facing = "D"
    coordenate_dict = {(0, 1): 'R', (0, -1): 'L', (1, 0): 'U', (-1, 0): 'D'}
    coordenates = []
    while (True):  
      count = 0
      for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni = start_x + di
        nj = start_y + dj    
        if 0 <= ni < rows and 0 <= nj < columns and matrix[ni][nj] == '0' and (ni, nj) != (previous_x, previous_y):
          if facing == "D":
            coordenate_dict[(0, 1)] = 'L F'
            coordenate_dict[(0, -1)] = 'R F'
            coordenate_dict[(1, 0)] = 'F'
            coordenate_dict[(-1, 0)] = 'F'
          if facing == "R":
            coordenate_dict[(0, 1)] = 'F'
            coordenate_dict[(0, -1)] = 'F'
            coordenate_dict[(1, 0)] = 'R F'
            coordenate_dict[(-1, 0)] = 'L F'
          if facing == "L":
            coordenate_dict[(0, 1)] = 'F'
            coordenate_dict[(0, -1)] = 'F'
            coordenate_dict[(1, 0)] = 'L F'
            coordenate_dict[(-1, 0)] = 'R F'
          if facing == "U":        
            coordenate_dict[(1, 0)] = 'F'
            coordenate_dict[(-1, 0)] = 'F'

          coordenates.append(coordenate_dict[(di, dj)])
          coordenate_dict = {(0, 1): 'R', (0, -1): 'L', (1, 0): 'D', (-1, 0): 'U'}  
          facing = coordenate_dict[(di, dj)]
          count = 0
          previous_x = start_x
          previous_y = start_y
          start_x = ni
          start_y = nj
        else:
          count += 1
      if count == 4:
        coordenates.append("E")
        break

    print(*coordenates)
  except EOFError:
    break