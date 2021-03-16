entrada = input()

lista = entrada.split()

frase = ''
for palavra in lista:
  for i in range(0, len(palavra)-1, 2):
    frase += palavra[i+1]
  frase += ' '  

print(frase)
