import re

while True:
  filename = input("Enter file: ")
  try:
    fhandle = open(filename)
  except:
    print("Not a valid file.")
    continue
  break

count = 0

numlist = list()

for line in fhandle:
  numbers = re.findall("([0-9]+)", line)
  if len(numbers) > 0:
    for i in range(len(numbers)):
      numlist.append(int(numbers[i]))

print("Numbers: ", len(numlist))

print("Sum: ", sum(numlist))