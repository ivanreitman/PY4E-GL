while True:
  try:
    filename = input("Please enter file name: ")
    if filename.lower() == "na na boo boo":
      print("NA NA BOO BOO TO YOU - You have been punk'd!")
      continue
    fhandle = open(filename)
  except:
    print("Not a valid file name.")
    continue
  break

subjects = 0

for line in fhandle:
  if not line.startswith("Subject:"):
    continue
  subjects = subjects + 1

print("There were", subjects, "subject lines in mbox.txt")