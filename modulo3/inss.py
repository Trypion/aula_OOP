import decimal

salario = float(input())

desconto = 0

if salario <= 720.00:
  desconto = salario*0.0765
elif 720.00 < salario <= 1200.00:
  desconto = salario*0.09
elif 1200.00 < salario <= 2400.00:
  desconto = salario*0.11
else:
  desconto = 2400*0.11

print(decimal.Decimal(round(desconto, 2)))