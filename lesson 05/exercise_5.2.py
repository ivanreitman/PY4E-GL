max = None
min = None

while True:
  raw = input("Enter a number: ")
  if raw == "done":
    break
  try:
    number = int(raw)
    if max is None:
      max = number
      min = number
    else:
      if number > max:
        max = number
      elif number < min:
        min = number
  except:
    print("Invalid input")
    continue

print("Maximum is", max)
print("Minimum is", min)