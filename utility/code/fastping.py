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
    p=Popen(['ping','-c 2',ip],stdout=PIPE)
#    print p.stdout.read()
    m = re.search('Request timeout', p.stdout.read(),re.IGNORECASE)
    if not m:
        print ip + " is alive"
    else:
        print ip + " is dead"

def ping2(ip):
    p=Popen(['ping','-c 2',ip],stdout=PIPE)
#    print p.stdout.read()
    m = re.search('Request timeout', p.stdout.read(),re.IGNORECASE)
    if not m:
        return True
    else:
        print "{0} is not arrived".format(ip)
        return False

if __name__ == '__main__':
    ping(sys.argv[1])