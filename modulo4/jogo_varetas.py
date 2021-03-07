tam = -1
while(tam != 0):
  tam = int(input())
  
  lista_de_varetas = []  
  
  for i in range(tam):
    ci, vi = [int(w) for w in input().split()]
    lista_de_varetas.append((ci, vi))

  quantidade_retangulos = 0

  quantidade_varetas = 0

  for vareta in lista_de_varetas:
    if vareta[1]%2 == 0:
      quantidade_varetas += vareta[1]
    else:
      quantidade_varetas += (vareta[1]-1)
  
  quantidade_retangulos = int(quantidade_varetas/4)
  print(quantidade_retangulos)