entradas = int(input())

lista = []

for i in range(entradas):
    salto1, salto2, salto3, atleta = [x for x in input().split()]

    lista.append({'salto1': salto1, 'salto2': salto2,
                  'salto3': salto3, 'atleta': atleta})

maior_salto = 0

for item in lista:
    maior_salto_do_atleta = max(
        [float(item['salto1']),
         float(item['salto2']),
         float(item['salto3'])]
    )
    if maior_salto_do_atleta > maior_salto:
        maior_salto = maior_salto_do_atleta
        nome_atleta = item['atleta']

print(nome_atleta)
