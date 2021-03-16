from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
try:
    while True:
        print('waiting for connection')
        tcpClisock, addr = tcpSerSock.accept()
        print(addr)
        while True:
            data = tcpClisock.recv(BUFSIZ)
            if not data:
                break
            tcpClisock.send(bytes(('[' + ctime() + ']' + ' ' + data.decode('utf-8')), 'utf-8'))

        tcpClisock.close()
except:
    tcpSersock.close()
