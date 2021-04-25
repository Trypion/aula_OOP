tam = int(input())
while(tam != 0):
  tempos = [int(w) for w in input().split(" ")]

  count = 10
  for i in range(len(tempos)-1):
    if tempos[i]+10 < tempos[i+1]:
      count += 10
    else:
      count += tempos[i+1]-tempos[i]  

  tam = int(input())

  print(count)