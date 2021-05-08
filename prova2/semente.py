tam, gotas = [int(w) for w in input().strip().split(" ")]

indices = input().strip().split(" ")

fita = []

for i in range(tam):
  fita.append(0)

for item in indices:
  fita[int(item)-1] = 1 

dias = 0
while 0 in fita:
  dias += 1

  temporario = fita.copy()
  for  i in range(tam):
    if fita[i] == 1:    
      if i != tam-1:
        temporario[i+1] = 1      
      if i != 0:
        temporario[i-1] = 1     
  
  fita = temporario.copy()

print(dias)
