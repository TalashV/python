from email.policy import HTTP
from platform import python_branch


Socket in python

import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) #'data.pr4e.org' - host ; 80 - port

HTTP

import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysock.close()


