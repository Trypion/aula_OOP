length = int(input())

for _ in range(length):
  words, music_len = [int(w) for w in input().strip().split(" ")]

  my_dict = {}
  for i in range(words*2):    
    if i%2 == 0:
      japonese_word = input()
      my_dict[japonese_word] = ''
    else:
      portuguese_word = input()
      my_dict[japonese_word] = portuguese_word

  music = []
  for _ in range(music_len):
    music.append(input().strip().split(" "))
  
  for lines in music:
    line = []
    for word in lines:
      try:
        line.append(my_dict[word])
      except KeyError:
        line.append(word)
    print(*line)

  print()
  