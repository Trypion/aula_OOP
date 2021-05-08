ordem = int(input())
P, Q, R, S, X, Y = [int(w) for w in input().strip().split(" ")]
K, Z = [int(w) for w in input().strip().split(" ")]

matriz_a = []
matriz_b = []
for i in range(1, ordem+1):
  linha_a = []
  linha_b = []
  for j in range(1, ordem+1):    
    linha_a.append((P*i + Q*j)%X)
    linha_b.append((R*i + S*j)%Y)
  matriz_a.append(linha_a)
  matriz_b.append(linha_b)

def multiplica_matrizes(a, b):
  m = len(a)
  n = len(b)
  p = len(b[0])

  c = []
  for i in range(m):
    c.append([0]*p)
    for j in range(p):
      soma = 0
      for k in range (n):
        soma += a[i][k] * b[k][j]
      c[i][j] = soma
  
  return c

matriz_c = multiplica_matrizes(matriz_a, matriz_b)
print(matriz_c[K-1][Z-1])