# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import glob
import os
import pdb

from conf.conf import ROOT
from conf.conf import REMOTE
from conf.conf import WEB
from conf.conf import UTILITY
from conf.conf import SQLMAP_PATH
from conf.conf import HYDRA_PATH
from conf.conf import WEAPON_DATABASE

from lib.cmdline import showAll
from lib.cmdline import cmdLineParser

from lib.common import readInput
from lib.common import enterAndExit
from lib.common import getUnicode
from lib.common import dataToStdout
from lib.common import valicateIp
from lib.common import valicateDomain
from lib.common import valicateCidr
from lib.common import listCIDR
from lib.common import inputMsg

from lib.xmlparser import xmlparser
from lib.threadpool import *

class TreadStone(object):
    """docstring for TreadStone"""

    def __init__(self):
        super(TreadStone, self).__init__()
        self.mod = None

    #功能：打印exp列表
    ##返回值：none  
    '''
    def showExpList(self):
        print "\n[*]please wait loading exp lists...\n[*]==exploit list=="
        lists = glob.glob(EXPLISTS)
        for _ in lists:
            if "__init__.py" not in _:
                print os.path.basename(_)

    def showPlugin(self):
        print "\n[!]please wait loading plugin...\n[!]==plugin list=="
        lists = glob.glob(PLUGINS)
        for _ in lists:
            if "__init__.py" not in _:
                print os.path.basename(_)
    '''

    #功能：打印exp信息
    ##返回值：none  
    def showInfo(self,name):
        '''
        print "[!]Name:" + self.mod.info['Name']
        print "[!]Description:" + self.mod.info['Description']
        print "[!]Author:" + self.mod.info['Author']
        print "[!]Product:" + self.mod.info['Product']
        print "[!]References:" + self.mod.info['References']
        print "[!]DisclosureDate:" + self.mod.info['DisclosureDate']
        '''
        for key in name:
            print key + ":  " + name[key]



    #功能：初始化exp
    ##返回值：exp 路径 + xml dic
    def initExp(self,name):

        xml = None
        key = None

        for key in WEAPON_DATABASE:
            if name in key:
                xml = xmlparser(ROOT+WEAPON_DATABASE[key][0])
                return key,xml
        return key,xml

        '''
        if os.path.exists(WEB+name):#/web/code/x.py
            #第一种动态加载module方法
            print "\n[*]Init web exploit..."
            return 0, "/exploits/web/code/" + name

        elif os.path.exists(EXP+name):#/exp/code/x.py
            print "\n[*]Init remote exploit..."
            return 1, "/exploits/exp/code/" + name
        else:
            if os.path.exists(PLUGINS+name):#/common/code/x.py
                print "\n[*]Init common tools..."
                return 2, "/exploits/common/code/" + name
            else:
                return 3, ""
        '''
            
        '''
        #不需要返回可以直接调用
        if mo:
            return exp#返回一个exp的类对象
        '''
        #第二种方法使用exec
        '''
        fp = open(exp_path).read()
        exec(fp)
        or 
        code = "\n"
        code + = "global exp\n"
        code + = "exp = tsExploits()\n"
        exec(code + fp)
        #
        '''
        
    #功能：执行脚本
    #返回值：none
    '''
    def execPlugin(self,plugin,host):
        print "[*]Loading plugins...\n"
        plugin_name = os.path.dirname(os.path.abspath(argS['self'])) + "/plugins/" + plugin
        if not os.path.exists(plugin_name):
            self.usages("plugin not exist")
        else:
            fp = open(plugin_name).read()
            exec(fp)
    ''' 

    #功能：执行
    ##返回值：none  
    def run(self):

        args = cmdLineParser()

        path,infoxml = self.initExp(args['exp'])

        if infoxml == None:
            print "\n[!]error, you input exploit do not exist"
            print "\n[*]All exploits list :"
            showAll()
            sys.exit(1)

        if args['mode'] == 'i':

            self.showInfo(infoxml)
            enterAndExit()

        else:
#            pdb.set_trace()
            target,tlist,plist,tnum = inputMsg()#target存储的时最原始未处理的输入目标信息
            tpool = Ethread(infoxml,path,tlist,plist,tnum,target)
            tpool.threadManager()

if __name__ == '__main__':

    treadstone = TreadStone()
    treadstone.run()
