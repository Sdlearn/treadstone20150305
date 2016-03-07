# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import re
import socket

# Encoding used for Unicode data
UNICODE_ENCODING = "utf8"

# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\?%02x"

def getUnicode(value, encoding=None, noneToNull=False):
    #reference https://github.com/sqlmapproject/sqlmap.git
    """
    Return the unicode representation of the supplied value:

    >>> getUnicode(u'test')
    u'test'
    >>> getUnicode('test')
    u'test'
    >>> getUnicode(1)
    u'1'
    """

    if noneToNull and value is None:
        return NULL

    if isListLike(value):
        value = list(getUnicode(_, encoding, noneToNull) for _ in value)
        return value

    if isinstance(value, unicode):
        return value
    elif isinstance(value, basestring):
        while True:
            try:
                return unicode(value, encoding or UNICODE_ENCODING)
            except UnicodeDecodeError, ex:
                try:
                    return unicode(value, UNICODE_ENCODING)
                except:
                    value = value[:ex.start] + "".join(INVALID_UNICODE_CHAR_FORMAT % ord(_) for _ in value[ex.start:ex.end]) + value[ex.end:]
    else:
        try:
            return unicode(value)
        except UnicodeDecodeError:
            return unicode(str(value), errors="ignore")  # encoding ignored for non-basestring instances

def isListLike(value):
    #reference https://github.com/sqlmapproject/sqlmap.git
    """
    Returns True if the given value is a list-like instance

    >>> isListLike([1, 2, 3])
    True
    >>> isListLike(u'2')
    False
    """

    return isinstance(value, (list, tuple, set))



def readInput(message, default=None, checkBatch=False):
    """
    Reads input from terminal
    """

    retVal = None

    message = getUnicode(message)

    if "\n" in message:
        message += "%s> " % ("\n" if message.count("\n") > 1 else "")
    elif message[-1] == ']':
        message += " "

    if retVal is None:
        if checkBatch:
            if isListLike(default):
                options = ",".join(getUnicode(opt, UNICODE_ENCODING) for opt in default)
            elif default:
                options = getUnicode(default, UNICODE_ENCODING)
            else:
                options = unicode()

            dataToStdout("\r%s%s\n" % (message, options), forceOutput=True, bold=True)

            retVal = default
        else:
            dataToStdout("\r%s" % message, forceOutput=True, bold=True)

            try:
                retVal = raw_input() or default
                retVal = getUnicode(retVal, encoding=sys.stdin.encoding) if retVal else retVal
            except :
                print "\nPress Enter to continue...",
                raw_input()
                raise

    return retVal



def dataToStdout(data, forceOutput=False, bold=False):
    """
    Writes text to the stdout (console) stream
    """

    message = ""

    if forceOutput:
        if isinstance(data, unicode):
            data = data or ""
            message = data.encode(sys.stdout.encoding)
        else:
            message = data

        sys.stdout.write(message)

        try:
            sys.stdout.flush()
        except IOError:
            pass


def enterAndExit():
    print "\nPress Enter to continue...",
    raw_input()
    
#reference https://github.com/AnthraX1/InsightScan
def valicateIp(target):
    reip = re.compile(r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$)')#127.0.0.1
    if reip.match(target):
        #处理ip地址
        return True
    else:
        return False

def valicateDomain(target):
    redomain = re.compile(r'([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?)')#www.baidu.com
    if redomain.match(target) and not '/' in target:
        return True
    else:
        return False

#reference https://github.com/AnthraX1/InsightScan
def valicateCidr(target):
    cidr = re.compile("^([0-9]{1,3}\.){0,3}[0-9]{1,3}(/[0-9]{1,2}){1}$")
    if cidr.match(target):
        # extract prefix and subnet size
        prefix, subnet = target.split("/")
        # each quad has an appropriate value (1-255)
        quads = prefix.split(".")
        for q in quads:
            if (int(q) < 0) or (int(q) > 255):
                print "[!]Error: quad "+str(q)+" wrong size."
                return False
        # subnet is an appropriate value (1-32)
        if (int(subnet) < 1) or (int(subnet) > 32):
            print "[!]Error: subnet "+str(subnet)+" wrong size."
            return False
        return True
    else:
        return False

# print a list of IP addresses based on the CIDR block specified
#reference https://github.com/AnthraX1/InsightScan
def listCIDR(target):
    cidrlist=[]
    parts = target.split("/")
    baseIP = ip2bin(parts[0])
    subnet = int(parts[1])
    # Python string-slicing weirdness:
    # "myString"[:-1] -> "myStrin" but "myString"[:0] -> ""
    # if a subnet of 32 was specified simply print the single IP
    if subnet == 32:
        print bin2ip(baseIP)
    # for any other size subnet, print a list of IP addresses by concatenating
    # the prefix with each of the suffixes in the subnet
    else:
        ipPrefix = baseIP[:-(32-subnet)]
        for i in range(2**(32-subnet)):
            cidrlist.append(bin2ip(ipPrefix+dec2bin(i, (32-subnet))))
        return cidrlist 
       
# convert an IP address from its dotted-quad format to its
# 32 binary digit representation
#reference https://github.com/AnthraX1/InsightScan
def ip2bin(ip):
    b = ""
    inQuads = ip.split(".")
    outQuads = 4
    for q in inQuads:
        if q != "":
            b += dec2bin(int(q),8)
            outQuads -= 1
    while outQuads > 0:
        b += "00000000"
        outQuads -= 1
    return b

# convert a binary string into an IP address
#reference https://github.com/AnthraX1/InsightScan
def bin2ip(b):
    ip = ""
    for i in range(0,len(b),8):
        ip += str(int(b[i:i+8],2))+"."
    return ip[:-1]

# convert a decimal number to binary representation
# if d is specified, left-pad the binary number with 0s to that length
#reference https://github.com/AnthraX1/InsightScan
def dec2bin(n,d=None):
    s = ""
    while n>0:
        if n&1:
            s = "1"+s
        else:
            s = "0"+s
        n >>= 1
    if d is not None:
        while len(s)<d:
            s = "0"+s
    if s == "": s = "0"
    return s



'''
'''
def inputMsg():
    tlist = []
    isdomain = None
    plist = []
    msg = "Welcome to treadstone project by zzt 2015\n"
    msg += "if you want to continue, Please enter the exploit targets, target could be ip [127.0.0.1]"
    msg += " or domian [www.baidu.com]\n"
    msg += "if you want exploit some targets one-time, please enter like [127.0.0.1/24]\nnow input your target:"
    msg += "\n default (192.168.1.1)"
    target = readInput(msg,"192.168.1.1")

    msg = "please enter port like [23 or 80,90 or 1-1024] default (80):"
    port = readInput(msg,80)

    msg = "Please enter thread number default (5):"
    num = readInput(msg,5)

    #先处理port，因为后面域名的需要
    if ',' in port:
        part = port.split(',')
        plist = [int(part[0]),int(part[1])]
    elif '-' in port:
        part = port.split('-')
        for p in range(int(part[0]),int(part[1])):
            plist.append(p)
    else:
        plist = [int(port)]

    if valicateIp(target):
        #处理ip地址
        tlist = [target]
    elif valicateDomain(target):
        for p in plist:
            #处理域名
            addr = socket.getaddrinfo(target,p)
            for ip in addr:
                tlist.append(ip[4][0])
            tlist = list(set(tlist))#去重
    elif valicateCidr(target):
        tlist = listCIDR(target)
    else:
        print "[!]Error input CIDR is wrong\n"
        sys.exit(1)
        

    return target,tlist,plist,num