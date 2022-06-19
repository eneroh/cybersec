#!/bin/sh
#requires root

for ip in $(cat iplist.txt); do nmap -sS -p 80 -T4 $ip; done
