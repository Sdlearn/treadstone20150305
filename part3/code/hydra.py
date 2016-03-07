
# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Use hydra tool to crack password
hydra -C password -M target ssh/ftp/telnet

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


ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))+'/../../output/'
pwlist = os.path.dirname(os.path.abspath(sys.argv[0]))+ '/PASSWORD.TXT'


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

def hydra(target,port):
    global q
    q = Queue.Queue()
#    pdb.set_trace()
    '''
    cmd = "rm -f " + ROOT + '/' + str(port) + '.txt'
    cmd1 = "rm -f " + ROOT + '/hydra.restore'

    cmd = []
    cmd.append("rm -f")
    p = Popen(['rm -f',ROOT + '/' + str(port) + '.txt'],stdout=PIPE)
    if p:
        print "Remove file!"
    p = Popen(['rm -f',ROOT + '/hydra.restore'],stdout=PIPE)
    if p:
        print "Remove tmp file!"

    '''

    if str(port) == '21':
        service = 'ftp'
    elif str(port) == '22':
        service = 'ssh'
    elif str(port) == '23':
        service = 'telnet'
    else:
        print "Now,this only support ftp(21) ssh(22) telnet(23) service!"
        sys.exit(0)

    tlist = listCIDR(target)

    #进行多进程处理
    '''
    #多进程效率不高，速度太慢
    p_recod = []
    for i in range(1,100):
        p = Process(target = scanport2, args = (port,))
        p.start()
        p_recod.append(p)

    for p in p_recod:
        p.join()
    '''
    for i in range(100):
        t = threading.Thread(target=scanport2, args=(port,))
        t.setDaemon(True)
        t.start()

    for _ in tlist:
        q.put(_)

    q.join()

    f = open(ROOT+str(port)+'.txt',"w")
    for ip in openlist:
        f.write(ip+"\n")
    f.close()

#    cmd = "xterm -e hydra -C %s -M %s %s" % (pwlist,ROOT+str(port)+'.txt',service)
#    print cmd
    cmd = "hydra -C %s -M %s %s > %shydra_result_%s.txt" % (pwlist,ROOT+port+'.txt',service,ROOT,port)
    os.system(cmd)
    print "[!]%s crack is done, please check result in [hydra_result_%s.txt]" % (service,port)

if __name__ == '__main__':
    '''
    global pfile
    pdb.set_trace()
    pfile  = readInput("Please, input password file\ndefault(PASSWORD.TXT):\n",pwlist)
    '''
    hydra(sys.argv[1],sys.argv[2])
