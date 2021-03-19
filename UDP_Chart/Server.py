from socket import *
from time import ctime
import _thread

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)
print(gethostbyname(gethostname()))
flag = False


def Sendback(addrto):
    global flag
    flag = True
    while True:
        data = input('>')
        if not data:
            flag = flag
            break
        udpSerSock.sendto(bytes(('[' + ctime() + ']' + ' ' + data), 'utf-8'), addrto)


if __name__ == '__main__':
    try:
        udpSerSock = socket(AF_INET, SOCK_DGRAM)
        udpSerSock.bind(ADDR)
        while True:
            data, addr = udpSerSock.recvfrom(BUFSIZ)
            print(addr, data.decode('utf-8'))
            if flag:
                continue
            _thread.start_new_thread(Sendback, (addr,))

    except:
        udpSerSock.close()
