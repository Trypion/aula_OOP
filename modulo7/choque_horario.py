from datetime import datetime

length = int(input())

grade = []
for i in range(length):
  grade.append(input().strip().split(" "))
  for j in range(1, len(grade[i])):
    grade[i][j] = {"weekday": grade[i][j][:1], "time": datetime.strptime(grade[i][j][1:-1], "%H%M"), "quantity":grade[i][j][-1]}

print(grade[0][1])