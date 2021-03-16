from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 11451
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        self.wfile.write(bytes('[' + ctime() + ']' + ' ', 'utf-8') + self.rfile.readline())


tcpServ = TCP(ADDR, MyRequestHandler)
tcpServ.serve_forever()
