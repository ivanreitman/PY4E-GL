# Based on Charles Severance's example code json2.py and geoxml.py from py4e.com
# Tested on http://py4e-data.dr-chuck.net/comments_42.json and http://py4e-data.dr-chuck.net/comments_1956546.json

import json

import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

numlist = []

while True:
  url = input("Enter url: ")
  print('Retrieving', url)
  try:
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
  except:
    print("Unable to retrieve.")
    continue
  break

print('Retrieved', len(data), 'characters')
# print(data.decode())

results = json.loads(data)

for i in range(len(results["comments"])):
  numlist.append(int(results["comments"][i]["count"]))

listsum = sum(numlist)

print("Count list:", numlist)
print("Sum:", listsum)