
# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Use whatweb tool 

'''
import os
import sys
import pdb
import Queue
import threading
import socket as sk

from common import listCIDR
from common import readInput
from multiprocessing import Process
from subprocess import Popen, PIPE


ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))+'/'
WHATWEB = '/Users/zzt/whatweb/whatweb'


def scanport2(port):
    global openlist 
    openlist = []
#    pdb.set_trace()
    while True:
        host = q.get()
        sd=sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        sd.settimeout(2)
        try:
            sd.connect((host,int(port)))     
            sd.close()
            openlist.append(host)
        except:
            pass
        q.task_done()

def whatweb(target,port):
    global q
    q = Queue.Queue()

    tlist = listCIDR(target)

    for i in range(1,100):
        t = threading.Thread(target=scanport2, args=(port,))
        t.setDaemon(True)
        t.start()

    for _ in tlist:
        q.put(_)

    q.join()

    f = open(ROOT+'whatweb_'+str(port)+'.txt',"w")
    for ip in openlist:
        f.write(ip+':'+port+"\n")
    f.close()

    cmd = "ruby %s --no-errors --input-file %s" % (WHATWEB,ROOT+'whatweb_'+port+'.txt')
#    cmd = "ruby %s --no-errors --input-file %s > whatweb_result_%s.txt" % (WHATWEB,ROOT+'whatweb_'+port+'.txt',port)
#    print cmd
    os.system(cmd)
    print "[!]port:%s web identify is done, please check result in [whatweb_result_%s.txt]" % (port,port)

if __name__ == '__main__':

    whatweb(sys.argv[1],sys.argv[2])
