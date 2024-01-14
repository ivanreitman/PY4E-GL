while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

letters = dict()

for line in fhandle:
  if len(line) > 0:
    line = line.lower()
    for character in list(line):
      if character.isalpha():
        letters[character] = letters.get(character, 0) + 1

sortedletters = sorted([(value,key) for (key, value) in letters.items()], reverse = True)

for count, letter in sortedletters:
  print(letter, count)