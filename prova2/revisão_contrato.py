element_to_remove = '-1'
element = '-1'

while(element_to_remove != '0' and element != '0'):
  element_to_remove, element = input().strip().split(" ")

  element = list(element)

  try:
    while element_to_remove in element:
      element.remove(element_to_remove)
  except ValueError:        
    pass

  if element == []:
    element.append('0')

  print(int("".join(element)))
