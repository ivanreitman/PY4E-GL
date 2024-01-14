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

# for key, value in writers.items():
#   print(key,value)

commits = [(value, key) for (key, value) in sorted(writers.items(),reverse = True)]

(value, key) = commits[0]

print(key, value)