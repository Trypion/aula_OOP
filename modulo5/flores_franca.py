frase = input()

while(frase != "*"):
  palavras = frase.split(" ")

  primeira_letra = palavras[0][0].lower()

  eh_tautograma = all(primeira_letra == palavra[0].lower() for palavra in palavras)

  print("Y" if eh_tautograma else "N")

  frase = input()
