import decimal

valor = float(input())
desc = input()
nasc = input()
idade = int(input())

tab_descontos = {"A": 0.30, "B": 0.20, "C": 0.10, "D": 0.05, "E": 0.0}

premio = 0
desconto = 0

premio += valor*0.10 if nasc == "nacional" else valor*0.15

desconto += premio*tab_descontos[desc]

desconto += premio*0.10 if idade > 24 else 0

print(decimal.Decimal(round(premio - desconto, 2)))