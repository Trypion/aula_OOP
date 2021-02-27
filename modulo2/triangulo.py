
a = float(input())
b = float(input())
c = float(input())

condicao1 = abs(b-c) < a < b+c
condicao2 = abs(a-c) < b < a+c
condicao3 = abs(a-b) < c < a+b

print(condicao1 or condicao2 or condicao3)

