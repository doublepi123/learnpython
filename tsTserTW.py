from twisted.internet import protocol, reactor
from time import ctime
PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
    def dataReceived(self, data: bytes):
        self.transport.write(ctime())
factory = protocol.Factory()
factory.protocol = TSServProtocol
reactor