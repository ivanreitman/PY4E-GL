sum = 0
count = 0

while True:
  raw = input("Enter a number: ")
  if raw == "done":
    break
  try:
    sum = sum + float(raw)
    count = count + 1
  except:
    print("Please enter a number.")
    continue

average = sum / count

print(sum, count, average)