nterms = int(input())+1

n1, n2 = 0, 1
count = 0

sequencia = []

while count < nterms:
    sequencia.append(n1)
    nth = n1 + n2

    n1 = n2
    n2 = nth
    count += 1

print(sequencia[-1])
