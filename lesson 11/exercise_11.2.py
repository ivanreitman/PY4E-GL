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

revision = list()

for line in fhandle:
  revnum = re.findall("^New Revision: ([0-9]+)", line)
  if len(revnum) > 0:
    revision.append(int(revnum[0]))
    count += 1

average = int(sum(revision)/len(revision))

print(average)