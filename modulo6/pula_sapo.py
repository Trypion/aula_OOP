altura, quantidade_canos = [int(i) for i in input().strip().split(" ")]
canos = [int(i) for i in input().strip().split(" ")] 

resultado = "YOU WIN"
for i in range(quantidade_canos-1):
  if canos[i+1] > canos[i]+altura:
    resultado = "GAME OVER"
    break

print(resultado)