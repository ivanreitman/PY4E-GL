# Based on Chuck Severance's code example. See bottom.
# Tested with http://data.pr4e.org/romeo.txt

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
  url = input("Enter URL: ")
  try:
    # print(url.split("/"))
    host = url.split('/')[2]
    # print(host)
    mysock.connect((host, 80))
    cmd = "GET " + url + " HTTP/1.0\r\n\r\n"
    cmd = cmd.encode()
    mysock.send(cmd)
  except:
    print("Unable to retrieve file.")
    continue
  break


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# Original Code: https://www.py4e.com/code3/socket1.py