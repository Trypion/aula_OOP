tam = int(input())

valores = []
quantidade = []
for _ in range(tam):
  valores.append(float(input()))
  quantidade.append(int(input())) 

saque = float(input())

i = len(quantidade)-1
lista_de_notas_sacadas = {}
notas_sacadas = 0
while(saque != 0):
  if valores[i] <= saque and quantidade[i] > 0:
    notas_sacadas += 1
    quantidade[i] -= 1
    saque -= valores[i]
  else:
    notas_sacadas = 0
    i -= 1
  lista_de_notas_sacadas[valores[i]] = notas_sacadas
  if(saque == 0 and i > 0):
      notas_sacadas = 0
      lista_de_notas_sacadas[valores[i-1]] = notas_sacadas

lista = list(lista_de_notas_sacadas.values())
lista.reverse()
print(*lista)
