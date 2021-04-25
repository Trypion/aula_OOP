tam = int(input())

lista = []

for i in range(tam+1): 
  especie = input().strip()    
  while(especie != ''):
    lista.append(especie)
    especie = input().strip()
  if especie == '' and len(lista)>0:    
    repetidas = {especie: round(lista.count(especie)*100/len(lista), 4) for especie in lista}
    ordenado = dict(sorted(repetidas.items()))
    for chave, valor in ordenado.items():
      print(f"{chave} "+'{:.4f}'.format(valor)) 
    if i != tam:
        print("")
    lista.clear()