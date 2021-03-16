from socket import *
import re

HOST = '127.0.0.1'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    print(ADDR)
    if not data:
        break
    print(data.decode('utf-8'))
