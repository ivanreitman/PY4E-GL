while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

writers = dict()

for line in fhandle:
  if len(line) > 0 and line.startswith("From "):
    words = line.split()
    if len(words) >= 2:
        writers[words[1]] = writers.get(words[1],0) + 1

emailnum = 0
author = ""

if len(writers) > 0:
  for i in writers:
    if writers[i] > emailnum:
      emailnum = writers[i]
      author = i

print(author, emailnum)