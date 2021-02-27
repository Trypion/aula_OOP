a, b, c = [int(i) for i in input().split()]
x, y, z = [int(i) for i in input().split()]

div3 = int(z/c)
div2 = int(y/b)
div1 = int(x/a)

print(div1*div2*div3)
