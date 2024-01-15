# Based on Chuck Severance's example code. See bottom.
# Tested on http://py4e-data.dr-chuck.net/known_by_Fikret.html and http://py4e-data.dr-chuck.net/known_by_Nick.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter original URL: ')
repeats = int(input("Enter number of repeats: "))
position = int(input("Enter number of position: "))

for i in range(repeats):
  print("Retrieving:", url)
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  tags = soup('a')
  
  url = tags[position - 1].get('href', None)
  lastname = tags[position - 1].contents[0]
  print("Last name retrieved:", lastname)


# Code: https://www.py4e.com/code3/urllinks.py