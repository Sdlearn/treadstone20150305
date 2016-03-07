# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
fast ping to dectect host alive
'''
import re
import sys
from subprocess import Popen
from subprocess import PIPE

def ping(ip):
    cmd = "ping %s" % ip
    p=Popen(['/opt/X11/bin/xterm','-e',cmd],stdout=PIPE)
#    print p.stdout.read()
    m = re.search('Request timeout', p.stdout.read(),re.IGNORECASE)
    if not m:
        print ip + " is alive"
    else:
        print ip + " is dead"

if __name__ == '__main__':
    ping(sys.argv[1])