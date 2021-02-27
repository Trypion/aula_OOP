
comprimento, distancia_pedagio = [int(i) for i in input().split()]
custo_km, custo_pedagio = [int(i) for i in input().split()]

custo_total = 0

numero_pedagio = round(comprimento/distancia_pedagio)

custo_total += custo_pedagio*numero_pedagio

custo_total += comprimento*custo_km

print(custo_total)
