while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

worddict = dict()

for line in fhandle:
  if len(line) > 0:
    words = line.split()
    for word in words:
      if word not in worddict:
        worddict.update({word : 0})

print(worddict.items())