# Based on Charles Severance's example code geoxml.py at py4e.com
# Tested on http://py4e-data.dr-chuck.net/comments_42.xml and http://py4e-data.dr-chuck.net/comments_1956545.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
tree = ET.fromstring(data)

results = tree.findall('comments/comment')

for i in range(len(results)):
  numlist.append(int(results[i].find('count').text))

listsum = sum(numlist)

print("Count list:", numlist)
print("Sum:", listsum)
    