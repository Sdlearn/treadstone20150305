# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Use nmap --open to identify port service
/opt/X11/bin/
'''
import sys
import os


def nmap(ip):

    cmd = "xterm -e nmap -T5 -A -O %s" % (ip) 

    os.system(cmd)

if __name__ == '__main__':
    nmap(sys.argv[1])