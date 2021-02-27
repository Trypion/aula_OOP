import decimal

valor = float(input())
sexo = input()
idade = int(input())

premio = 0

premio = valor*0.10

if sexo == "M":
  if 25 <= idade <= 33:
    premio -= premio*0.1
  elif idade > 33:
    premio -= premio*0.2

if sexo == "F":
  if idade <= 24:
    premio -= premio*0.05
  elif 25 <= idade <= 33:
    premio -= premio*0.2
  else:
    premio -= premio*0.35

print(decimal.Decimal(round(premio, 2)))