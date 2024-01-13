while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

vocab = []

for line in fhandle:
  if len(line) > 0:
    words = line.rstrip().split()
  else:
    continue
  for word in words:
    if word not in vocab:
      vocab.append(word)

vocab.sort()

print(vocab)