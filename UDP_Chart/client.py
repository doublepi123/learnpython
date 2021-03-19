from socket import *
from time import ctime
import _thread
HOST = '127.0.0.1'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

def Listen():
    Data, addr = udpCliSock.recvfrom(BUFSIZ)
    print(ADDR)
    print(Data.decode('utf-8'))
while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(bytes(('[' + ctime() + ']' + ' ' + data), 'utf-8'), ADDR)
    _thread.start_new_thread(Listen,())

