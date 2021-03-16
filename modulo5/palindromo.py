import re
frase = input()
frase_limpa = "".join(re.findall("[a-zA-Z]+", frase))
print(frase_limpa == frase_limpa[::-1])