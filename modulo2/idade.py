idade_em_dias = int(input())

anos = int(idade_em_dias/365)

dias_restantes = (idade_em_dias%365)

meses = int(dias_restantes/30)

dias = int(dias_restantes%30)

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
