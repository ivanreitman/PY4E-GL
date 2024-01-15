# Based on Chuck Severance's code example. See bottom.
# Tested with http://data.pr4e.org/romeo.txt
# Already implemented header skipping in exercise_12.2.py

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

file = b""

while True:
    data = mysock.recv(512)
    file += data
    if len(data) < 1:
        break
    # print(data.decode(),end='')

mysock.close()

file = file.decode()

file = file[file.index("\r\n\r\n") + 4:]

# print(repr(file))

charlength = min([len(file),3000])

print(file[:charlength])

print("That was the first", charlength, "characters.")

print("Total characters:", len(file))

# Original Code: https://www.py4e.com/code3/socket1.py