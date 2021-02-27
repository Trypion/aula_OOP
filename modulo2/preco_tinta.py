import decimal

preco = 25.00
litros = 3.6
area = 18

area_galao = area*litros

preco_pagar = 0

area_pintar = int(input())

numero_galoes = round(area_pintar/area_galao)

if numero_galoes < 1:
  numero_galoes = 1

preco_pagar = numero_galoes*preco

print(f'- área de cobertura: {area_pintar}')
print(f'- número de galões: {numero_galoes}')
print(f'- valor a ser pago: R$ {round(decimal.Decimal(preco_pagar), 2)}')