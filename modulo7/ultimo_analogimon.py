while True:
  try:    
    rows, columns = [int(w) for w in input().strip().split(" ")]

    matrix = []
    for _ in range(rows):
      matrix.append([int(w) for w in input().strip().split(" ")])


    initial_position = ()
    pokemon_position = ()
    for idx_row, row in enumerate(matrix):
      for idx_column, element in enumerate(row):
        if element == 1:
          initial_position = (idx_row,idx_column)
        if element == 2:
          pokemon_position = (idx_row,idx_column)

    time_to_get_pokemon = abs(initial_position[0] - pokemon_position[0]) + abs(initial_position[1] - pokemon_position[1])

    print(time_to_get_pokemon)
  
  except EOFError:
    break