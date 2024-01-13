# modified from Chuck Severance's example

while True:
  filename = input("Enter a file name: ")
  try:
    fhand = open(filename)
  except:
    print("Not a valid file name.")
    continue
  break

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 : continue
    if words[0] != 'From' : continue
    print(words[2])