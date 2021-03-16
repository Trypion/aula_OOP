num = float(input())

if num > 0:
    num = '+' + format(num, ".4E")
else:
    num = format(num, ".4E")

print(num)
