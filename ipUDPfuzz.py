#!/usr/bin/python

from scapy.all import *

send(fuzz(IP("1.1.1.1"))/ICMP()/fuzz(UDP()),loop=1)

#Working
