# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import time
import sys

HYDRA_PATH = ""
SQLMAP_PATH = ""
PYTHON = "/usr/bin/python"

ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
WEB = ROOT + r"/exploits/web/code/"
UTILITY = ROOT + r"/utility/code/"
REMOTE = ROOT + r"/exploits/remote/code/"


# Encoding used for Unicode data
UNICODE_ENCODING = "utf8"

# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\?%02x"

VERSION = "1.0-dev"
VERSION_STRING = "treadstone/%s%s" % (VERSION, "-%s" % time.strftime("%Y%m%d", time.gmtime(os.path.getctime(__file__))))

WEAPON_DATABASE = {
	#web vulnerability
	'/exploits/web/code/bash_rce.py' : ['/exploits/web/Zimbra-bash-rce.xml','Zimbra mail system bash remote command exeution'],
	'/exploits/web2/code/eyou4_del_addition_unlink.py' : ['/exploits/web2/Eyou4_del_unlink.xml','eyou 4.0 mail system unlink file vulnerability'],
	'/exploits/web2/code/eyou4_list_userinfo_sql_inject.py' : ['/exploits/web2/Eyou4_list_userinfo_sql_inject.xml','eyou 4.0 list_userinfo.php sql injection vulnerability'],
	'/exploits/web2/code/eyou4_search_lastlogin_sql_inject.py' : ['/exploits/web2/Eyou4_search_lastlogin_sql_inject.xml','eyou 4.0 search_lastlogin.php sql injection vulnerability'],
	'/exploits/web2/code/eyou5_em_controller_action_help_class_sql_inject.py' : ['/exploits/web2/Eyou5_controller_help_sql_inject.xml','eyou 5.0 sql injection vulnerability'],
	#remote command execution
	'/exploits/remote/code/ABunreal.py' : ['/exploits/remote/AB-Unreal-Server.xml','AB Unreal Server remote buffer overflow'],
	'/exploits/remote/code/ExploitActFax.py' : ['/exploits/remote/ActFax-FTP-Server.xml','Actfax ftp remote buffer overflow'],
	'/exploits/remote/code/NOMBRE.py' : ['/exploits/remote/Apache-Mod-JK.xml','Apache Tomcat JK Web Server Stack-based buffer overflow'],
	'/exploits/remote/code/avayawinpdm.py' : ['/exploits/remote/Avaya-winpdm.xml','Avaya-winpdm Stack-based buffer overflow'],
	'/exploits/remote/code/avguard.py' : ['/exploits/remote/Avira-Guard.xml','Avira AntiVir personal edition avguard.exe 7.00.00.52 local heap overflow'],
	'/exploits/remote/code/BigAnt_Server_version_2.50_XPLT.py' : ['/exploits/remote/BIG-Ant-Server-XPLT.xml','BigAnt Server version 2.50 SEH Overwrite - 0day remote buffer overflow'],
	'/exploits/remote/code/ExploitBIGAntServer.py' : ['/exploits/remote/BIG-Ant-Server.xml','BigAnt Server 2.52 remote buffer overflow'],
	'/exploits/remote/code/bftp_bof.py' : ['/exploits/remote/Bison-FTP-Server-MKD.xml','BisonFTP Server v3.5(MKD) Remote Buffer Overflow'],
	'/exploits/remote/code/bisonftpserver.py' : ['/exploits/remote/Bison-FTP-Server.xml','BisonFTP Server v3.5 Remote Buffer Overflow'],
	'/exploits/remote/code/bopup.py' : ['/exploits/remote/Bopup-Com-Server.xml','Bopup Communications Server (3.2.26.5460) Remote BOF Exploit (SEH)'],
	'/exploits/remote/code/ca_bof_poc.py' : ['/exploits/remote/CA-ArcServe.xml','CA ArcServe remote buffer overflow '],
	'/exploits/remote/code/cerberusftpserver-overflow.py' : ['/exploits/remote/Cerberus-FTP-Server.xml','Cerberus FTP Server 4.0.9.8 (REST) Remote Buffer Overflow'],
	'/exploits/remote/code/codeweb.py' : ['/exploits/remote/CoDeSyS-SCADA-Server.xml','CoDeSyS SCADA Exploit'],
	'/exploits/remote/code/Cogent-datahub.py' : ['/exploits/remote/Cogent-Datahub.xml','ogent Datahub v7.1.1.63 Remote Unicode Buffer Overflow Exploit'],
	'/exploits/remote/code/diskpulseserver-overflow.py' : ['/exploits/remote/Disk-Pulse-Server.xml','Disk Pulse Server v2.2.34 stack-based buffer overflow'],
	'/exploits/remote/code/EasyFTPServer1.7.11.py' : ['/exploits/remote/Easy-FTP-Server-1.7.11.xml','Easy FTP Server USER Command Remote Buffer Overflow'],
	'/exploits/remote/code/EChat-Server-v2.5.py' : ['/exploits/remote/EChat-Server-v2.5.xml','EChat Server remote buffer-overflow vulnerability'],
	'/exploits/remote/code/freefloatftpACCL.py' : ['/exploits/remote/Free-Float-FTP-ACCL.xml','Free Float FTP Server ACCL Command Remote Buffer Overflow'],
	'/exploits/remote/code/freefloatftpREST.py' : ['/exploits/remote/Free-Float-FTP-REST.xml','Free Float FTP Server ACCL Command Remote Buffer Overflow'],
	'/exploits/remote/code/FreeFloatFTPServer.py' : ['/exploits/remote/Free-Float-FTP-Server.xml','Free Float FTP Server USER Command Remote Buffer Overflow'],
	'/exploits/remote/code/ftpgetter.py' : ['/exploits/remote/FTP-Getter.xml','FTP-Getter Remote Buffer Overflow'],
	'/exploits/remote/code/dsmcad.py' : ['/exploits/remote/IBM-Tivoli-Storage.xml','IBM Tivoli Storage Manager Express 5.3 CAD Service Buffer Overflow'],
	'/exploits/remote/code/kingview.py' : ['/exploits/remote/KingView-Scada.xml','KingView 6.5.3 SCADA HMI allow remote attackers to cause a DoS or execute arbitrary code'],
	'/exploits/remote/code/knftpserver.py' : ['/exploits/remote/KnFTP-Server.xml','KnFTP-Server knftpd.exe'],
	'/exploits/remote/code/kolibry.py' : ['/exploits/remote/Kolibri-Server.xml','Kolibri v2.0 is vulnerable to a remote buffer overflow'],
	'/exploits/remote/code/ldap_server_0day.py' : ['/exploits/remote/LDAP-Server.xml','Alpha Centauri Software SIDVault LDAP Server remote root exploit'],
	'/exploits/remote/code/sapmaxdb-exec.py' : ['/exploits/remote/SAP-Server-MaxDB.xml','Sap Server 7.7.06.09 is vulnerable to a remote buffer overflow attack'],
	'/exploits/remote/code/SavantWebServer.py' : ['/exploits/remote/Savant-Web-Server.xml','Savant Server is prone to a remote buffer-overflow vulnerability'],
	'/exploits/remote/code/scriptftp33.py' : ['/exploits/remote/Script-FTP-3.3.xml','ScriptFTP 3.3 Remote Buffer Overflow (LIST)'],
	'/exploits/remote/code/sdpDownloader.py' : ['/exploits/remote/SDP-Downloader.xml','SDP Download from http://sdp.ppona.com/ suffer a Remote Buffer Overflow'],
	'/exploits/remote/code/simplehttpd142.py' : ['/exploits/remote/Simple-HTTPD.xml','Simple-HTTPD Remote root on sfr/ubiquisys femtocell webserver (wsal/shttpd/mongoose)'],
	'/exploits/remote/code/solarftpPASVexploit.py' : ['/exploits/remote/Solar-FTP-Server.xml','Stack-Based buffer overflow in Solar FTP 2.1.1 PASV for Windows'],
	'/exploits/remote/code/sysaxmulti.py' : ['/exploits/remote/Sysax-multi.xml','A boundary error in the SYSAX multi server 5.50 Create Folder Buffer Overflow'],
	'/exploits/remote/code/TFTP_Server1.4ST.py' : ['/exploits/remote/TFTP-Server-1.4ST.xml','stack-Based buffer overflow in TFTP Server SP 1.4 for Windows'],
	'/exploits/remote/code/uplusftp-overflow.py' : ['/exploits/remote/UPlus-FTP-Server.xml','UPlus FTP server 1.7 is prone to a buffer overflow'],
	'/exploits/remote/code/Vermillion_FTP_Deamon_v1.31_Remote_BOF_Exploit.py' : ['/exploits/remote/Verm-FTP-Daemon.xml','Stack-Based buffer overflow in Vermillion FTP Deamon 1.31 for Windows'],
	'/exploits/remote/code/XlightServer3.7.0.py' : ['/exploits/remote/XlightFTP-Server-v3.7.0.xml','XlightFTP Server v3.7.0 Remote Root BOF Exploit'],
	'/exploits/remote/code/XMEasyPersonalFtp.py' : ['/exploits/remote/XM-Personal-FTP-Server.xml','XM FTP Server Command Remote Buffer Overflow Exploit'],
	'/exploits/remote/code/YourOpenPersonalWEBSERVER_DCA-00015.py' : ['/exploits/remote/YourPersonalWebServer.xml','YOPS (Your Own Personal [WEB] Server) is a small SEDA-like HTTP Remote Buffer Overflow'],
	#client side 
	'/exploits/client/code/adobeflashmp4.py' : ['/exploits/client/Adobe-Flash-Mp4.xml','dobe Flash Player before 10.3.183.5 on Windows, Mac OS X, Linux, and Solaris and before 10.3.186.3 on Android, and Adobe AIR before 2.7.1'],
	'/exploits/client/code/ExploitAudiotran.py' : ['/exploits/client/AudioTran-PLS.xml','Audiotran 1.4.1 Win XP SP2/SP3 English Buffer Overflow Stack Overflow / SEH'],
	'/exploits/client/code/aviosoftdigital.py' : ['/exploits/client/Aviosoft-Digital.xml','Aviosoft 1.x Win 7 and XP SP2/SP3 English Buffer Overflow Stack Overflow'],
	'/exploits/client/code/CoreFTP.py' : ['/exploits/client/Core-FTP-Server.xml','core ftp The vulnerability can be triggered by convincing a user to submit an overly long String for the SSH password'],
	'/exploits/client/code/gomplayer.py' : ['/exploits/client/GOM-Player.xml','GOM-Player buffer overflow'],
	'/exploits/client/code/sidvault_ldap.py' : ['/exploits/client/LDAP-Vault.xml','SidVault 2.0e client side buffer overflow'],
	'/exploits/client/code/ExploitMSExcel.py' : ['/exploits/client/Microsoft-Excel-Record.xml','Microsoft Excel is prone to a buffer-overflow vulnerability'],
	'/exploits/client/code/microsoft-visio.py' : ['/exploits/client/Microsoft-Visio.xml','Drawing Exchange Format (DXF) is a kind of data file format for CAD which is designed by Autodesk for cooperation'],
	'/exploits/client/code/ExploitMSWord.py' : ['/exploits/client/Microsoft-Word-Record.xml','Microsoft Word is prone to a buffer-overflow vulnerability'],
	'/exploits/client/code/ExploitQuickPlayer.py' : ['/exploits/client/Quick-Player.xml','Quick Player is prone to a buffer-overflow vulnerability'],
	'/exploits/client/code/WMMaker.py' : ['/exploits/client/Windows-Movie-Maker.xml','Windows-Movie-Maker client side buffer overflow'],
	#ddos tools
	'/exploits/dos/code/DenialOfService80.py' : ['/exploits/dos/Denial-Of-Service.xml','This Denial Of Service tool uses raw IP packets in no-novel ways to try stress the web target'],
	#utility tools
	'/utility/code/fastping.py' : ['/utility/fastping.xml','Fast ping utility to identify host is alvie or not'],
	'/utility/code/portscan.py' : ['/utility/portscan.xml','Use tcp connection to identify port is open or not'],
	'/utility/code/subbrute.py' : ['/utility/subbrute.xml','sub dns brute tool'],
	'/utility/code/nmap.py' : ['/utility/nmap.xml','nmap tool'],
	'/utility/code/xsscrapy.py' : ['/utility/xsscrapy.xml','xss scanner tool'],
	'/utility/code/rsync.py' : ['/utility/rsync.xml','rsync unauthorized scanner tool'],
	'/utility/code/svn.py' : ['/utility/svn.xml','svn leak scanner tool'],
	#part3
	'/part3/code/hydra.py' : ['/part3/hydra.xml','hydra tool'],
	'/part3/code/whatweb.py' : ['/part3/whatweb.xml','whatweb tool'],
	'/part3/code/test.py' : ['/part3/test.xml','test']
}

BANNER = '''
                    -O$-                                   CCCCC>                                                        
            ---     -C$                                   C$         --                                                  
        CCCCCCCCOCCCCO-                                  CC?      ?OCCCCO!                                               
       CC?!::!CO77>>:                                    C$!     CC?   CQ-                                               
     -C?     COQ                                        CC$     CC7    C$    CC7                                         
     C?      CC$                                        CCC     CO-    CC   :C$:                                         
    7O-      CC7      !>  OC?   :>!         -7C       :!CC>    !CO-    C7   CC$        ->>-      !!   -!       ->!       
    C$      >C$!    :CCQ CCC! >CCCC7     7CCCCC     7COCCC-    !CC>       !7CC$77:    CCCCO>   >CCO  COC7     OCCC?      
    CO>     CC$    CCCCOCO:  ?O> CC$    OO!!OC!    CO: >CQ      CCO!      >7CC?77-  ?C7  CC$  C?CC7?C7CC?   !C7 CC$      
    CCQ-    CCC   C? CCCC-  -CC  CC?   C?  -C$-   CO:  CC$      OCCO-       CO-     CQ   CCC!C7 CCCO- CC!   CQ  CCO      
     CO-    CC>      CC$    CC: ?OO   C$   CC$   -CC   CC?       CCCO!     CCQ     CC7   >CC>   CCO  >C$-  CC?  O$-      
            OC-     7CC>   -CQ 7CO   CC7   CC?   C$:   CO!        CCC$     CCO    -CQ:   !CC!  ?CC:  CC$   CO!:OO:       
           CCQ      CC$    CC$OC-    CQ-   CO!  7CO   ?CQ-         CCC7    CC7    CCQ    7CC-  OO$   CC?  OC$CO!         
           COO      CC7    COO      CCC   CCQ-  CO7   OCO           CC$   7CQ-    CC$    CCQ   CC7  >CQ:  CC$-           
           CC7      CC!    CC?    - CC?   CCO   CC!   CC7           CC$   CC$   : CC$    CC7   CO!  CC$   CCO    -       
          CC$:     !C$    !CC?  7C7 CCC  CCC? C>CC>  CCC! CC>       CC?   COC :O? CCQ:  7OC   CCQ-  CC? C>CCO   CO       
          CC$      CC$    -CC$>CC?  CC$7COCCOO? CCOCC?CCCCCC$:      CO:   CC$CC7  CCC?  C$    CCO   CC?CC CCO7CCC-       
       -CCCCCCCC   CCC     CCCCO-   CCCC7 COO>  CCCO!>CCO:?CC?     CC7    CCCO-    CCCCC7     CC7   CCO7  CCCOO!         
        :----::-            !>:      :>-  !>     !!-  !!   CCO:  -CO>      !:       :>!-       -    -!-    :>:           
                                                            !COCCC!                                                                                                                                                                           
	'''


BANNER_1 = {
1 :
'''
TreadStone is best!
     /@
    \ \\
  ___> \\
 (__O)  \\
(____@)  \\
(____@)   \\
 (__o)_    \\
       \    \\

''',
2 :
"""
    \\ - - //
     ( @ @ )
┏━━━━━━━━━oOOo-(_)-oOOo━┓
┃ TreadStone, 
             Welcome!!!!┃
┃          Oooo  ┃
┗━━━━━━━━━ oooO━-(   )━┛
    (   )    ) /
     \ (    (_/
      \_)
""",
3 :
"""
　　　　　　　`-^--'`<　　 '　　　　 
　　　　　　 (_.)　_　)　 /　　　　　
treadstone, `.___/`　　/　　　　　
Are you ready?  -----' /　　　　　　
　 <------.　　 __ / __　 \　　　　　　
　 <------l====O)))==) \) /====　　　　
　 <------'　　`--' `.__,' \　　　　　 
　　　　　　　　 l　　　　l　　　　　 
　　　　　　　　 \　　　 /


""",
4 :
"""
　　　　　　 _//|.-~~~~-, 
　　　  　　 /66　\　　　 \_@ 
　　   ●）(")_　 / 
     （┃　　'--'|| |-\　/ Don't be worry!
     				TreadStone help you! 　　　 
　　 　
""",
5 :
"""
╭︿︿︿╮ 
{/ o  o /}  
 ( (oo) )   
  ︶ ︶︶  Don't be stupid!
╭︿︿︿╮
{/ $  $ /}
 ( (oo) ) 
 ︶ ︶ ︶  User is god!
 treadstone: "Use me right now!"
"""
}
