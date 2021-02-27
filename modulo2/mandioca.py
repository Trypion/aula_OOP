porcoes = []

for i in range(5):
  porcoes.append(int(input()))

porcoes[0] = porcoes[0]*300
porcoes[1] = porcoes[1]*1500
porcoes[2] = porcoes[2]*600
porcoes[3] = porcoes[3]*1000
porcoes[4] = porcoes[4]*150

print(sum(porcoes)+225)
