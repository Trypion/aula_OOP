while(True):
  try:
    rows, columns = [int(w) for w in input().strip().split(" ")]

    coffe_quantity = 0
    for i in range(rows):
      coffe_quantity += sum([int(w) for w in input().strip().split(" ")])
          
  except EOFError:
    break

  coffe_bags = coffe_quantity//60
  remain_coffe = coffe_quantity%60
  print(f"{coffe_bags} saca(s) e {remain_coffe} litro(s)")