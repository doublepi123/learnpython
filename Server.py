from socket import *
from time import ctime
import _thread

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)
print(gethostbyname(gethostname()))
def Sendback():
    while True:
        data = input('>')
        udpSerSock.sendto(bytes(('[' + ctime() + ']' + ' ' + data), 'utf-8'), addr)
try:
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)
    while True:
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        print(addr,data.decode('utf-8'))
        _thread.start_new_thread(Sendback,())

except:
    udpSerSock.close()
