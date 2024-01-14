import re

grep = input("Enter a regular expression: ")

fhandle = open("mbox.txt")

count = 0

for line in fhandle:
  line = line.rstrip()
  if re.search(grep, line):
    count += 1

print("mbox.txt had", count, "lines that matched", grep)