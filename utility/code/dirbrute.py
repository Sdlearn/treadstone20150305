#-*- coding:utf-8 -*-
#!/usr/bin/python
import re
import os
import sys
import Queue
import threading
import requests

dir_file = os.path.dirname(os.path.abspath(sys.argv[0])) + '/dir.txt'
out_file = os.path.dirname(os.path.abspath(sys.argv[0])) + '/../../output/'

def Worker(hostinfo):
    while True  
        uri = in_q.get()
        url = hostinfo + uri
        r = requests.head(url)
        if r.status_code == 200 or r.status_code == 301 or r.status_code == 302:
            out_list.append((url,r.status_code))
        in_q.task_done()

def dirbrute(host,port):
    global in_q,out_list
    dir_list = []
    out_list = []
    in_q = Queue.Queue()
    try:
        dir_list = open(dir_file).readlines()   
    except:
        print "File not found: %s" % dir_file

    if not re.search("http://",host,re.IGNORECASE):
        hostinfo = "http://" + host + ":" + port

    for i in range(100):
        worker = threading.Thread(target=Worker,args=(hostinfo,))
        worker.setDaemon(True)
        worker.start()

    for l in dir_list:
        l.strip()
        in_q.put(l)

    in_q.join()
    
    out_file += "exist_url_" + port + ".txt" 
    f = open(out_file,'w')  
    for ext_url in out_list:
        f.write(ext_url)
        print ext_url

    f.close()
    print "[!]Check out result in %s" % out_file

if '__name__' == '__main__':
    dirbrute(sys.argv[1],sys.argv[2])
