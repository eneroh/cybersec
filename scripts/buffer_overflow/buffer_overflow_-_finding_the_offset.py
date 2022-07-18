#!/usr/bin/python

import sys, socket

offset = ""

try:
    s=socket.socket(socket.AF_INET.socket.SOCK_STREAM
    s.connect(('192.168.1.90',9999))
    s.send(('TRUN //.:/' + offset))
    s.close()

except:
    print "Error connecting to server"
    sys.exit()
