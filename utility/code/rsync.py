# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import re
import sys
import pdb

from subprocess import Popen
from subprocess import PIPE

from fastping import ping2
from portscan import scanport

def rsync(addr,port="873"):
#    pdb.set_trace()
    if ping2(addr):
        if scanport(addr,port):
            #rsync 192.168.0.1::
            p=Popen(['rsync',ip,"::"],stdout=PIPE)
            m = re.search('Connection refused', p.stdout.read(),re.IGNORECASE)
            if m == None:
                print "{0}:{1}".format(addr,"rsync is open and vulnerable!")



def main():
    rsync(sys.argv[1])

if __name__ == '__main__':
    main()