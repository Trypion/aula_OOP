gabarito = input()
resposta = input()

acertos = 0
table = zip(gabarito, resposta)

for correta, resp in table:
    if correta == resp:
      acertos += 1

print(acertos)
