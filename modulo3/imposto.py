salario = float(input())
dep = int(input())

inss = 0
aliquota = 0
deducao = 0
desc_dep = dep*137.99

if salario <= 720.00:
  inss = salario*0.0765
elif 720.00 < salario <= 1200.00:
  inss = salario*0.09
elif 1200.00 < salario <= 2400.00:
  inss = salario*0.11
else:
  inss = 2400*0.11

if 1372.81 < salario <= 2743.25:
  aliquota = 0.15
  deducao = 205.92
if salario > 2743.25:
  aliquota = 0.275
  deducao = 548.82

irrf = (salario - desc_dep - inss)*aliquota-deducao

if irrf < 0:
  irrf = 0 

print(irrf)