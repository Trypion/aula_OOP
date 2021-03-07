quantidade = int(input())

lista = []

for i in range(quantidade):
  nome, distancia = [w for w in input().split(';')]
  lista.append({"nome": nome, "distancia": distancia})

praias_entre_15_20 = 0
distacia_media = 0
maior_distancia = 0


for item in lista:
  if float(item['distancia']) > maior_distancia:
    praia_mais_distante = item['nome']
    maior_distancia = float(item['distancia'])
  distacia_media += float(item['distancia'])
  if 15 <= float(item['distancia']) <= 20:
    praias_entre_15_20 += 1

distacia_media = round((distacia_media/quantidade), 1)

print(f"{praia_mais_distante};{praias_entre_15_20};{distacia_media}")

