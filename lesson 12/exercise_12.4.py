# Based on Chuck Severance's code. See bottom.
# Tested on https://www.crummy.com/software/BeautifulSoup/bs4/doc/ (489  paragraphs)
# and https://packaging.python.org/en/latest/tutorials/installing-packages/ (71 paragraphs)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Count paragraph tags
tags = len(soup('p'))

print("Number of paragraphs:", tags)

# Code: https://www.py4e.com/code3/urllinks.py