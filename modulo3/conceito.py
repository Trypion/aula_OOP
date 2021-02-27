a = float(input())
b = float(input())
c = float(input())

media = int(((a+b+c)/3)*10)

if media in range(90, 101):
  print("Ótimo")
elif media in range(75, 90):
  print("Bom")
elif media in range(60, 75):
  print("Satisfatório")
else:
  print("Insuficiente")
