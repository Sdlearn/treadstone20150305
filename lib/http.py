# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
import urllib
import urllib2
import gzip
import zlib
import pdb
import chardet #判断html的编码方式

from StringIO import StringIO

#HTTP请求类
#处理HTTP请求类，对具体方法进行封装
class HttpRquest(object):
    """docstring for HttpRquest"""
    def __init__(self):
        super(HttpRquest, self).__init__()

    # deflate support
    #功能：解密deflate加密数据
    #返回值：解密后的data
    def deflate(data):   # zlib only provides the zlib compress format, not the deflate format;
        try:               # so on top of all there's this workaround:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        except zlib.error:
            return zlib.decompress(data)

    #功能：调用具体API进行HTTP请求，并处理title编码
    #返回值：字典变量webresponse
    def httpRquest(self,host,req):
        webresponse = self.getWebResponse(host,req,1)
        
        webresponse['html'] = self.getUtf8Html(webresponse['html'])
        if webresponse['html']:
            match = re.search("<title>(.*?)<\/title>",webresponse['html'],re.IGNORECASE)
            if match:
                webresponse['title'] = self.getUtf8Html(match.group(1))

        return webresponse

    #功能：根据不同的HTTP方法获得统一编码后的HTML等信息
    #返回值：字典变量resp，包含所需的信息
    def getWebResponse(self,hostinfo,req,timeout):
        resp = {'error':'', 'html':''}
        #resp = {}
        #print resq['code']
#        pdb.set_trace()
        resp['host'] = hostinfo[0]
        resp['port'] = hostinfo[1]
        host = hostinfo[0]+':'+str(hostinfo[1])
        
#        print "\n[!]log hostinfo " + host

        #处理“http://”
        if not re.search("http://",host,re.IGNORECASE):
            url = "http://" + host + req['uri']
        else:
            url = host + req['uri']

        resp['url'] = url
        
            
        #url编码，判断url中是否包含%
        if not re.search("%",url):
            urllib.quote(url)
            
        #暂时不支持https
        #判断HTTP方法 GET OR POST
        if req['method'] == 'GET':
            data = req['data'] = ''#此时req['data']为空
            header = req['header']

        #post方法时应对data进行URLencoding
        if req['method'] == 'POST':
            data = urllib.urlencode(req['data'])
            header = req['header']

        #url中必须包含http://，不然报错
        rep = urllib2.Request(url=url,data=data,headers=header)
        resp['error'] = ''

        try:
            response = urllib2.urlopen(rep,timeout=timeout)
        except urllib2.URLError,e:
            resp['error'] = e.reason
            return resp

        #获取URL请求的返回状态码
        resp['code'] = response.code


        if resp['code'] == 200:
            #获得头信息
            resp['header'] = str(response.headers)
            if response.headers.get('Content-Encoding') == 'gzip':
                #处理gzip加密返回
                gz = gzip.GzipFile(fileobj=StringIO(response.read()),mode=r)
                resp['html'] = gz.read()
            elif response.headers.get('Content-Encoding') == 'deflate':
                #处理deflate加密返回
                #
                gz = StringIO( self.deflate(response.read()))
                resp['html'] = urllib2.addinfourl(gz, response.headers, response.url, response.code).read()
            else:
                #无加密返回
                resp['html'] = response.read()

        #判断URL跳转的情况，此时resp['html']应该为空
        if resp['code'] == 301 or resp['code'] == 302:
            resp['redirecturl'] = response.geturl()

        return resp


    #功能：将HTML内容中的非utf-8编码转化为utf-8编码
    #返回值：统一编码后的HTML
    def getUtf8Html(self,html):
        #通过调用chardet类判断返回的HTML的编码方式
        #其返回为字典的数据结构
        myChar = chardet.detect(html)
        if myChar['encoding'] != 'utf-8' or myChar['encoding'] != 'UTF-8':
            return html.decode('gb2312','ignore').encode('utf-8')
        else:
            return html

if __name__ == '__main__':
    pass
else:
    global treadstone_http
    treadstone_http = HttpRquest()