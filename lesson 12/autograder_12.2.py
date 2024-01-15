# Based on Chuck Severance's code example. See below.
# Tested on http://py4e-data.dr-chuck.net/comments_42.html and http://py4e-data.dr-chuck.net/comments_1956543.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

numlist = []

for tag in tags:
  if len(tag) > 0:
    #print('TAG:',tag)
    #print('URL:',tag.get('href', None))
    #print('Contents:',tag.contents)
    #print('Attrs:',tag.attrs)
    numlist.append(int(tag.contents[0]))

numsum = sum(numlist)

print("Sum:", numsum)

# Code: https://www.py4e.com/code3/urllink2.py