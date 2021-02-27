segundos = int(input())

m, s = divmod(segundos, 60)

h, m = divmod(m, 60)

print(f'{h}:{m}:{s}')
