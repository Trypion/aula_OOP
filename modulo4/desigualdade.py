def calc_fatorial(n):
  b = n

  for i in range(n-1, 1, -1):  
    b = b*(i)

  return b

for i in range(100):
  if calc_fatorial(i) > i**10:
    res = i
    break

print(res)