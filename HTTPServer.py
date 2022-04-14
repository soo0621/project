#!/usr/bin/python3

import socket

host = ''
port = 10621
BUFF_SIZE = 4096
BACKLOG = 5

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_sock.bind((host, port))
serv_sock.listen(BACKLOG)

while True:
    print('lisening on port %s ...'%port)
    client_sock, client_address = serv_sock.accept()
    request = client_sock.recv(BUFF_SIZE)
    if request:
        print(request.decode())
        http_response = "HTTP/1.1 200 ok\r\nContent-Type : "\
                            "text/html\r\n\r\n"\
                            "<HTML><BODY><H1> Hello, World! </H1></BODY></HTML>"
        try:
            client_sock.sendall(http_response.encode())
        except:
            pass
    client_sock.close()

sock.close()
