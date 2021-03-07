x = int(input())
y = int(input())

count = 0

def verifica_primo(numero):
  primo = True
  
  if numero == 1:
    return False

  for i in range(2, numero):
    if numero%i == 0:
      primo = False
 
  return primo

for i in range(x, y+1):
  count += 1 if verifica_primo(i) == True else 0
  

print(count)