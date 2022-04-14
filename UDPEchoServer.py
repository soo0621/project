#!/usr/bin/python3

import socket

host = ''
port = 10621
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)

while True:
    print("\nwaiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0],client_address[1]))
    print("echo message : {}".format(message.decode()))


    if message.isdigit() == True:
        if int(message)%2 == 0:
            mess = ("{}는 짝수입니다.".format(message.decode()))
        elif int(message)%2 == 1:
            mess = ("{}는 홀수입니다.".format(message.decode()))
    elif message.isdigit() == False:
        mess = ("{}는 정수가 아닙니다.".format(message.decode()))

    sock.sendto(mess.encode(), client_address)

sock.close()
