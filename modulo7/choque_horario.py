from datetime import datetime, timedelta

length = int(input())

grade = []
for i in range(length):
  grade.append(input().strip().split(" "))
  for j in range(1, len(grade[i])):
    grade[i][j] = {"weekday": grade[i][j][:1], "time": datetime.strptime(grade[i][j][1:-1], "%H%M"), "quantity":grade[i][j][-1]}


def check_grade(grade):
  for i in range(len(grade)-1):    
    for j in range(1, len(grade[i])):      
      for z in range(1, len(grade)):
        for k in range(1, len(grade[z])):
          if grade[i][j]["weekday"] == grade[z][k]["weekday"]:            
            current_class_start_time = grade[i][j]["time"]
            current_class_end_time = current_class_start_time + timedelta(minutes=45*int(grade[i][j]["quantity"]))
            next_class_start_time = grade[z][k]["time"]
            next_class_end_time = next_class_start_time + timedelta(minutes=45*int(grade[z][k]["quantity"]))
            if next_class_start_time <= current_class_start_time <= next_class_end_time:
              return (grade[i][0], grade[z][0])
            elif next_class_start_time <= current_class_end_time <= next_class_end_time:
              return (grade[i][0], grade[z][0])
            elif current_class_start_time <= next_class_start_time <= current_class_end_time:
              return (grade[i][0], grade[z][0])
            elif current_class_start_time <= next_class_end_time <= current_class_end_time:
              return (grade[i][0], grade[z][0])

  return None         
          
print(*check_grade(grade))        