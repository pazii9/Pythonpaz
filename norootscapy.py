#!/usr/bin/python

from scapy.all import *
from socket import *
sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(("1.1.1.1", 53))
dnsQ = DNS(rd=1, qd =DNSQR(qname="ynet.co.il"))

dnsstring = str(dnsQ)
sock.send(dnsstring)
ls(DNS(sock.recv(4096)))
