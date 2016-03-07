#-*- coding:utf-8 -*-
#!/usr/bin/python
import re
import sys
import requests

svn_text = '/.svn/entries'


def svn_leak(host,port):

    if not re.search("http://",host,re.IGNORECASE):
        hostinfo = "http://" + host + ":" + port

    url = hostinfo + svn_text
    r = requests.head(url)
    if r.status_code == 200 :
        print "{0} has svn leak vulnerablity\nyou can visit url:\n{1}".format(host,url)

if '__name__' == '__main__':
    svn_leak(sys.argv[1],sys.argv[2])
