import re

cpf = input()
cpf = "".join(re.findall('[0-9]+', cpf))

def verifica_cpf(cpf):
  if all(num == cpf[0] for num in cpf):
    return False

  soma = 0
  seq = 10
  for x in list(cpf[:-2]):  
    soma += int(x)*seq
    seq -= 1

  primeiro_dig = soma*10%11
  
  soma = 0
  seq = 11
  for x in list(cpf[:-2]):
    soma += int(x)*seq
    seq -= 1
  
  soma += primeiro_dig*2
  segundo_dig = soma*10%11

  return True if (str(primeiro_dig)+str(segundo_dig)) == cpf[-2:] else False
 
print(verifica_cpf(cpf))