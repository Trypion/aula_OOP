tam = int(input())

for _ in range(tam):
  num1, op, num2, igual, resposta = [w for w in input().strip().split(" ")]

  if (op == '+'):
    resp_correta = int(num1) + int(num2)
  elif (op == '-'):
    resp_correta = int(num1) - int(num2)
  else:
    resp_correta = int(num1) * int(num2)  

  diferenca = resp_correta - int(resposta)

  print(f"E{'r'*abs(diferenca)}ou!")
