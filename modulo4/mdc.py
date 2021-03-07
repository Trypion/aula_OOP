n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

a = n1
b = n2
while b > 0:
    resto = a % b;
    a = b
    b = resto
    
print(a)