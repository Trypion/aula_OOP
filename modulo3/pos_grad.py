nota1 = input()
nota2 = input()
nota3 = input()
nota4 = input()

dict_notas = {"A": 4, "B": 3, "C": 2, "E": 0}

media = (dict_notas[nota1]+dict_notas[nota2]+dict_notas[nota3]+dict_notas[nota4])/4

print(media > 2)
