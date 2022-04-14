#!/usr/bin/python3

import socket
from os.path import exists
import os

host = ''
port = 10622
BUFF_SIZE = 1024
server_address = (host, port)

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(server_address)
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속했습니다')

filename = connectionSock.recv(BUFF_SIZE)
print('받은 데이터 : ', filename.decode('utf-8'))
data_transf = 0

f = open(filename, 'rb')
try:
    data = f.read(BUFF_SIZE)
    while data:
        data_transf += connectionSock.send(data)
        data = f.read(BUFF_SIZE)
    f.close()
except Exception as ex:
    print(ex)
print("전송완료 %s, 전송량 %d" %(filename.decode('utf-8'), data_transf))
myFile = open(filename, 'r')
line = myFile.readline()
c=0
while line != "":
    c+=1
    print("{} : {}".format(c,line))
    line = myFile.readline()

serverSock.close()
connectionSock.close()
