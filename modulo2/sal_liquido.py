import decimal

normais = float(input())
extras = float(input())

sal_bruto = 2500.00
sal_liquido = 2500.00

if normais < 200:  
  sal_bruto = (2500/200)*normais

if extras > 0:
  sal_bruto += ((2500/200)*extras)*1.20

ir = sal_bruto*0.13
inss = sal_bruto*0.09

sal_liquido = sal_bruto - (ir + inss)

print(f'- Salário Bruto : R$ {round(decimal.Decimal(sal_bruto), 2)}')
print(f'- IR (13%) : R$ {round(decimal.Decimal(ir), 2)}')
print(f'- INSS (9%) : R$ {round(decimal.Decimal(inss), 2)}')
print(f'- Salário Líquido : R$ {round(decimal.Decimal(sal_liquido), 2)}')