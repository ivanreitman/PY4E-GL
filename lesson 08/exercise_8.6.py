numlist = []
while True:
  raw = input("Enter a number: ")
  if raw.lower() == "done":
    break
  try:
    numlist.append(int(raw))  
  except:
    print("Invalid input")
    continue

if len(numlist) > 0:
  print("Maximum is", max(numlist))
  print("Minimum is", min(numlist))