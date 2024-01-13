while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

counter = 0

for line in fhandle:
  if not line.startswith("From "):
    continue
  words = line.split()
  if len(words) < 2:
    continue
  print(words[1])
  counter = counter + 1

print("There were", counter, "lines in the file with From as the first word")