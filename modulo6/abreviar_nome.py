nome = input().split(" ")

for i in range(1, len(nome)-1):
    if(len(nome[i]) > 3):
        nome[i] = nome[i][0]+'.'

print(" ".join(nome))
