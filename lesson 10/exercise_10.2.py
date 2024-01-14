while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

hours = dict()

for line in fhandle:
  if len(line) > 0 and line.startswith("From "):
    words = line.split()
    if len(words) >= 6:
        hour = words[5].split(":")[0]
        hours[hour] = hours.get(hour,0) + 1

for (hour, count) in sorted(hours.items()):
  print(hour,count)