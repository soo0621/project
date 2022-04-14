import socket

host = '203.250.133.88'
port = 10622
BUFF_SIZE = 1024

server_address = (host, port)
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(server_address)

print('연결에 성공했습니다.')
filename = input('전송할 파일 이름을 입력하세요: ')
clientSock.sendall(filename.encode('utf-8'))

data = clientSock.recv(BUFF_SIZE)
data_transf = 0

accessmode = 'wb'

f = open(filename,accessmode)
try:
    while data:
        f.write(data)
        data_transf += len(data)
        data = clientSock.recv(BUFF_SIZE)
    f.close()
except:
    print("파일이 존재하지 않습니다.")

myFile = open(filename, 'r', encoding='utf-8')
li = myFile.readline()
c = 0
while li != "":
    c += 1
    print("{} : {}".format(c, li))
    li = myFile.readline()

print('파일 {} 받기 완료. 전송량 {}'.format(filename, data_transf))




clientSock.close()