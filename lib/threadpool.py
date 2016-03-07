# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import Queue
import sys
import pdb
import threading
import importlib
import time
import datetime
#sys.path.append("../")
#import subprocess

from conf.conf import PYTHON
from conf.conf import ROOT
from conf.conf import WEAPON_DATABASE
from lib.common import valicateCidr

from subprocess import Popen, PIPE

from Queue import Queue
from multiprocessing import Process

q = Queue()
def importRun(xml):
#    print "\nimportRun thread exec"
#    print xml
    mod = importlib.import_module('exploits.web.code.'+ xml['CodeName'][:-3])#动态加载exploits目录下的exp module
    '''
    if mod:
        print "import success\n"
    '''
    while True:
        host,port=q.get()
        '''
        print "\nhost:" + host
        print "\nport:" + str(port)
        '''
        try:
#            pdb.set_trace()
            if mod.exp.vulnerable((host,port)):
                msg = "[!]" + host + " may be exploited!\n"                    
            else:
                msg = "[!]" + host + " may not be exploited!\n"
                               
            #self.lock.acquire()
            print msg
            #self.lock.release()
        except Exception, e:
            time.sleep(0.1)
            q.put((host,port))
            print "\n[!]import Error: " + str(e)
            #sys.exit(0)
        q.task_done()  

def execFile(path):
    #print "\nexecFile thread exec"

    while True:
#        pdb.set_trace()
        cmdline = []
        host,port=q.get()
#       xsscrapy.py 必须要进入该目录，再想想
        os.chdir(os.path.dirname(ROOT+path))
               
        ''' 
        cmd = PYTHON + " " + ROOT + path + " " + host + " " + str(port)

        print os.system(cmd)


        '''
#        pdb.set_trace()
        cmdline.append(PYTHON)
        cmdline.append(ROOT+path)
        cmdline.append(host)
        cmdline.append(str(port))

        
        try:
            #p=Popen(cmdline, stdout=PIPE)
            p  = Popen(cmdline, stdout=PIPE)

            out = p.communicate()[0]
           
            print out.strip('\n')
            '''
            if p:                                   
                print p.stdout.read().strip('\n')
            '''
        except Exception, e:
            time.sleep(0.1)
            q.put((host,port))
            #print "\n[!]execFile Error: " + str(e)
        
        q.task_done() 

def part3(path,target):

#    pdb.set_trace()
    while True:
        cmdline = []
        port = q.get()

        cmdline.append(PYTHON)
        cmdline.append(ROOT+path)
        cmdline.append(target)
        cmdline.append(str(port)) 
        try:
            p=Popen(cmdline, stdout=PIPE)
            #p  = Popen(cmdline)
            if p:
                print p.stdout.read().strip('\n')
        except Exception, e:
            time.sleep(0.1)
            q.put(port)
            print "\n[!]part3 Error: " + str(e)
        q.task_done()

class Ethread():
    def __init__(self,xml,path,tlist,plist,num,target):
        self.xml = xml
        self.tlist = tlist
        self.plist = plist
        self.num = num
        self.mod = None
#        self.lock = Lock()
        self.path = path
        self.target = target


    def threadManager(self):
#        pdb.set_trace()
        if self.xml['Type'] == 'web':

            if len(self.tlist) < self.num:
                self.num = len(self.tlist)

            for i in range(int(self.num)):
                t = threading.Thread(target=importRun, args=(self.xml,))
                t.setDaemon(True)
                t.start()   
                 
            for ip in self.tlist:
                for port in self.plist: 
                    q.put((ip,port))
            q.join()#等待队列为空在执行其他操作
        elif self.xml['Type'] == 'part3':

            if not valicateCidr(self.target):
                print "[!]Error: check your input, example: 127.0.0.1/24"
                sys.exit(0)

            if len(self.plist) < self.num:
                self.num = len(self.plist)

            for i in range(int(self.num)):
                t = threading.Thread(target=part3, args=(self.path,self.target,))
                t.setDaemon(True)
                t.start()

            for port in self.plist:
                q.put(port)

            q.join()
            

        else:

            if len(self.tlist) < self.num:
                self.num = len(self.tlist)

            for i in range(int(self.num)):
                t = threading.Thread(target=execFile, args=(self.path,))
                t.setDaemon(True)
                t.start()   
                 
            for ip in self.tlist:
                for port in self.plist: 
                    q.put((ip,port))
            q.join()
         






