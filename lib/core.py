# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
from lib.http import treadstone_http


#[{'request': {'a': 'b'}}, {'response':{'c': 'd'}}]
#
#攻击扫描类
#根据expinfo传递的内容进行扫描和自动化利用
class Exploit(object):
    """docstring for Exploit"""
    def __init__(self, expinfo):
        super(Exploit, self).__init__()
        #初始化唯一的数据，接收exp中的信息
        self.expinfo = expinfo

    #功能：执行其他脚本
    #返回值：none
    def run(self,host):
        pass
        
    #验证是否存在漏洞
    #返回值：True or False
    def vulnerable(self,host):

        if self.excute_scan(host):
            return True
        else:
            return False

    #功能：执行扫描任务
    #返回值：True or False
    def excute_scan(self,host):
        for step in self.expinfo['ScanSteps']:#循环内部逻辑不够完整，现在只有一次request情况
            if 'Request' in step:
                resp = treadstone_http.httpRquest(host,step['Request'])
                if not resp['error']:
                    if self.check_response(resp,step['ResponseTest']):
                        return True
                    else:
                        return False
                else:
                    print "\n[!]error "
                    print resp['error']


    #功能：对HTTP response进行验证
    #返回值：True or False
    def check_response(self,response,test):
        if self.check_one(response,test):
            return True
        else:
            return False

    #功能：调用具体的验证方法，根据type属性进行分类验证，item和group
    #返回值：True or False
    def check_one(self,response,test):
        if test['type'] == 'item':
            if self.check_item(response,test):
                return True
            else:
                return False
        else:
            if self.check_group(response,test):
                return True
            else:
                return False
    
    #功能：单点验证
    #返回值：True or False  
    def check_item(self,response,test):
        if test['varibale'] == '$code':
            return self.test_int(test['operator'],int(response['code']),int(test['value']))
        elif test['varibale'] == '$body':
            return self.test_string(test['operator'],response['html'],test['value'])
        elif test['varibale'] == '$head':
            return self.test_string(test['operator'],response['header'],test['value'])

    #功能：多点验证，根据operator进行逻辑计算
    #返回值：True or False
    def check_group(self,response,test):
        if test['operator'] == 'AND':
            for item in test['checks']:
                if not self.check_one(response,item):
                    return False
            return True
        elif test['operator'] == 'OR':
            for item in test['checks']:
                if self.check_one(response,item):
                    return True
            return False

    #功能：验证int类型
    #返回值：True or False
    def test_int(self,operator,val,expect_val):
        if operator == '==':
            return val == expect_val
        elif operator == '!=':
            return val != expect_val
        elif operator == '>':
            return val > expect_val
        elif operator == '<':
            return val < expect_val
        elif operator == '>=':
            return val >= expect_val
        elif operator == '<=':
            return val <= expect_val

    #功能：验证字符串类型
    #返回值：True or False
    def test_string(self,operator,val,expect_val):
        if operator == 'start':
            reg = '^' + expect_val
            match = re.search(reg,val,re.IGNORECASE)
            if match:
                print "regex rule: \n%s" % reg
                print "regex match: \n%s" % match.group()
                return True
        elif operator == 'end':
            reg = '$' + expect_val
            match = re.search(reg,val,re.IGNORECASE)
            if match:
                print "regex rule: \n%s" % reg
                print "regex match: \n%s" % match.group()
                return True
        elif operator == 'contain':
            match = re.search(expect_val,val,re.IGNORECASE)
            if match:
                print "regex rule: \n%s" % expect_val
                print "regex match: \n%s" % match.group()
                return True
        elif operator == 'regex':
            match = re.search(expect_val,val,re.IGNORECASE)
            if match:
                print "regex rule: \n%s" % expect_val
                print "regex match: \n%s" % match.group()
                return True
        




