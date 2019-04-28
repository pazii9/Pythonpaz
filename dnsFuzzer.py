#!/usr/bin/python

from scapy.all import *
ipAddress="1.1.1.1"

send(IP(dst=ipAddress)/fuzz(DNS()),loop=1)
