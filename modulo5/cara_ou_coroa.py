import re

tam = int(input())

while tam != 0:  
  resultados = input()

  cara = re.findall('[0]+', resultados)
  coroa = re.findall('[1]+', resultados)

  maria = len(cara)
  joao = len(coroa)

  print(f"Mary won {maria} times and John won {joao} times")
  tam = int(input())