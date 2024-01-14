while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

school = dict()

for line in fhandle:
  if len(line) > 0 and line.startswith("From "):
    words = line.split()
    if len(words) >= 2:
        school[words[1].split("@")[1]] = school.get(words[1].split("@")[1],0) + 1

print(school)