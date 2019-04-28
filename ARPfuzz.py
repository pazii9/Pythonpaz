#!/usr/bin/python

from scapy.all import *

send(IP(dst="1.1.1.1")/fuzz(ARP()),loop=1)

#Working
