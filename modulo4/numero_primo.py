numero = int(input())

primo = True

for i in range(2, numero):
  if numero%i == 0:
    primo = False
    break

if numero == 1:
  primo = False

print(primo)
