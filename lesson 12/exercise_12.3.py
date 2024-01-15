# Based on Chuck Severance's code example. See bottom.
# Tested with http://data.pr4e.org/romeo.txt and https://www.w3.org/Protocols/rfc2616/rfc2616.txt

import urllib.request

while True:
  url = input("Enter URL: ")
  try:
    fhand = urllib.request.urlopen(url)
  except:
    print("Unable to retrieve file.")
    continue
  break

file = ""

for line in fhand:
    # print(line.decode().strip())
    file += line.decode()

charlength = min([len(file),3000])

print(file[:charlength])

print("That was the first", charlength, "characters.")

print("Total characters:", len(file))

# Original Code: https://www.py4e.com/code3/socket1.py and https://www.py4e.com/code3/urllib1.py