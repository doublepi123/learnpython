from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)
print(gethostbyname(gethostname()))
try:
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)
    while True:
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto(bytes(('[' + ctime() + ']' + ' ' + data.decode('utf-8')), 'utf-8'), addr)
except:
    udpSerSock.close()
