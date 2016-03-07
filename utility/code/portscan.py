
# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Use tcp connection to identify port is open or not
'''
import sys
import pdb
import socket as sk

def scanport(host,port):
#    pdb.set_trace()
    sd=sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    sd.settimeout(5)
    try:
        sd.connect((host,int(port)))
    	print "%s:%s OPEN" % (host, port)
    	#print host + ":" + port + " OPEN"
        sd.close()
        return True
    except Exception,e:
    	print "[!]Error:%s:%s %s" % (host,port,str(e))
        return False
        


if __name__ == '__main__':
    scanport(sys.argv[1],sys.argv[2])
  