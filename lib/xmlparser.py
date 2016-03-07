# -*- coding: utf-8 -*-
#!/usr/bin/python
import xml.dom.minidom
from xml.dom.minidom import parse

def xmlparser(name):

    xmlinfo = {}
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(name)
    module = DOMTree.documentElement

    exploit = module.getElementsByTagName("Exploit")[0]

    # 打印详细信息
    xmlinfo['NameXML'] = exploit.getAttribute("NameXML")
    xmlinfo['CodeName'] = exploit.getAttribute("CodeName")
    xmlinfo['Platform'] = exploit.getAttribute("Platform")
    xmlinfo['Service'] = exploit.getAttribute("Service")
    xmlinfo['Type'] = exploit.getAttribute("Type")
    xmlinfo['RemotePort'] = exploit.getAttribute("RemotePort")
    xmlinfo['LocalPort'] = exploit.getAttribute("LocalPort")
    xmlinfo['ShellcodeAvailable'] = exploit.getAttribute("ShellcodeAvailable")
    xmlinfo['ShellPort'] = exploit.getAttribute("ShellPort")
    xmlinfo['SpecialArgs'] = exploit.getAttribute("SpecialArgs")
    

    info = module.getElementsByTagName("Information")[0]
    xmlinfo['Author'] = info.getAttribute("Author")
    xmlinfo['Date'] = info.getAttribute("Date")
    xmlinfo['Vulnerability'] = info.getAttribute("Vulnerability")
    xmlinfo['Information'] = info.childNodes[0].data

    target = module.getElementsByTagName("Targets")[0]
    xmlinfo['Targets'] = target.childNodes[0].data

    return xmlinfo
    
    