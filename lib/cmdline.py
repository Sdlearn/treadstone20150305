# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import sys
import re

from optparse import OptionParser
from optparse import OptionError

from lib.common import getUnicode
from lib.common import enterAndExit
from conf.conf import VERSION_STRING
from conf.conf import WEAPON_DATABASE

def cmdLineParser():

    usage = "python treadstone.py exp_name mode"
    
    parser = OptionParser(usage=usage)

    try:
        parser.add_option("--hh", dest="advancedHelp",action="store_true",help="Show advanced help message and exit")
        parser.add_option("--showall", dest="showAll",action="store_true",help="Show all exploits and exit")
        parser.add_option("--search", dest="keyWord",help="search keyword for exploits show and exit")
        parser.add_option("-v","--version", dest="showVersion",action="store_true",help="Show program's version number and exit") 

        argv = []
        options = {}
        prompt = False

        for arg in sys.argv:
            
            argv.append(getUnicode(arg, encoding=sys.getfilesystemencoding()))

        try:
            (args, _) = parser.parse_args(argv)
        except UnicodeEncodeError, ex:
            print "\n[!] %s" % ex.object.encode("unicode-escape")
            raise SystemExit

        if '--hh' in argv:
            parser.print_help()
            showModes()
            raise SystemExit

        if '--showall' in argv:
            showAll()
            raise SystemExit

        if '--search' in argv:
            searchKey(args.keyWord)
            raise SystemExit

        if args.showVersion:
            print VERSION_STRING
            raise SystemExit

        if len(_) <= 2:
            parser.print_help()
            raise SystemExit

        options['exp'] = _[1]#module name
        options['mode'] = _[2]
        

        if options['mode'] not in ('i','e'):
            showModes()
            raise SystemExit

        return options

    except (OptionError, TypeError), e:
        print parser.error(e)

    except SystemExit:
        print "\nPress Enter to continue...",
        raw_input()
        raise

#功能：打印运行模式
##返回值：none  
def showModes():
    print "\noptions mode:\n[!]i\t:\tshow exp/module infomation\n[!]e\t:\texploit vulnerability/execute module"     

def showAll():
    i = j = k =l = m = n = 0
    print "\n[!]Web exploits list\n"
    for key in WEAPON_DATABASE:
        if '/exploits/web' in key: 
            i += 1          
            print key + "           " + WEAPON_DATABASE[key][1]

    print "\n[!]Remote exploits list\n"
    for key in WEAPON_DATABASE:
        if '/exploits/remote' in key:
            j += 1
            print key + "           " + WEAPON_DATABASE[key][1]

    print "\n[!]Client side exploits list\n"
    for key in WEAPON_DATABASE:
        if '/exploits/client' in key:
            k +=1
            print key + "           " + WEAPON_DATABASE[key][1]

    print "\n[!]Ddos exploits list\n"
    for key in WEAPON_DATABASE:
        if '/exploits/dos' in key:
            l +=1
            print key + "           " + WEAPON_DATABASE[key][1]

    print "\n[!]Utility exploits list\n"
    for key in WEAPON_DATABASE:
        if '/utility/code' in key:
            m +=1
            print key + "           " + WEAPON_DATABASE[key][1]

    print "\n[!]part3 tools list\n"
    for key in WEAPON_DATABASE:
        if '/part3/code' in key:
            n +=1
            print key + "           " + WEAPON_DATABASE[key][1]

    print """
            =[  {0}  ]
+ -- --=[ {1} exploits - {2} remote - {3} client ]
+ -- --=[ {4} dos - {5} auxiliary - {6} part3      ]
    """.format(VERSION_STRING,i,j,k,l,m,n)

def searchKey(keyword):
    for key in WEAPON_DATABASE:
        if re.search(keyword,WEAPON_DATABASE[key][1],re.IGNORECASE):
            print key + "           " + WEAPON_DATABASE[key][1]

    