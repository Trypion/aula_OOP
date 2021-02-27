origem = input()
temperatura = float(input())
destino = input()

def converte_temp(origem, temp, destino):
    if origem == "c":
        if destino == "f":
            print(temp*1.8+32)
        elif destino == "k":
            print(temp+273.15)
        else:
            print((temp+273.15)*1.8)

    if origem == "f":
        if destino == "c":
            print((temp-32)/1.8)
        if destino == "k":
            print((temp+459.67)*(5/9))
        else:
            print(temp+459.67)

    if origem == "k":
        if destino == "c":
            print(temp-273.15)
        if destino == "f":
            print(temp*9/5-459.67)
        else:
            print(temp*9/5)

    if origem == 'r':
        if destino == 'c':
            print((temp-491.67)*(5/9))
        if destino == 'f':
            print(temp-459.67)
        else:
            print(temp*5/9)


converte_temp(origem, temperatura, destino)

