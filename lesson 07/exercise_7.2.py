while True:
  try:
    filename = input("Enter file name: ")
    fhandle = open(filename)
  except:
    print("Not a valid file name.")
    continue
  break

spamtotal = 0
spamcounter = 0

for line in fhandle:
  if not line.startswith("X-DSPAM-Confidence:"):
    continue
  spamtotal = spamtotal + float(line[len("X-DSPAM-Confidence:"):].strip())
  spamcounter = spamcounter + 1
  # print(line, spamtotal)

print("Average spam confidence:", spamtotal / spamcounter)
