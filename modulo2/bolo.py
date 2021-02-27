xicaras, ovos, leite = [int(i) for i in input().split()]

xicaras_max = 2
ovos_max = 3
leite_max = 5

divisoes = []

divisoes.append(int(xicaras/xicaras_max))
divisoes.append(int(ovos/ovos_max))
divisoes.append(int(leite/leite_max))

print(min(divisoes))
