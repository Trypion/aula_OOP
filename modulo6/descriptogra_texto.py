normal = list(input().strip())
cifragem = list(input().strip())
mensagem = list(input().strip())

decodificada = ''

for letra in mensagem:  
  decodificada += normal[cifragem.index(letra)] if letra.isalpha() else letra

print(decodificada)