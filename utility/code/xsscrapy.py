#!/usr/bin/env python

import re
import sys
import pdb
import argparse
from scrapy.cmdline import execute
from xsscrapy.spiders.xss_spider import XSSspider

__author__ = 'Dan McInerney'
__license__ = 'BSD'
__version__ = '1.0'
__email__ = 'danhmcinerney@gmail.com'

'''
def get_args():
    parser = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-u', '--url', help="URL to scan; -u http://example.com")
    parser.add_argument('-l', '--login', help="Login name; -l danmcinerney")
    parser.add_argument('-p', '--password', help="Password; -p pa$$w0rd")
    parser.add_argument('-c', '--connections', default='30', help="Set the max number of simultaneous connections allowed, default=30")
    parser.add_argument('-r', '--ratelimit', default='0', help="Rate in requests per minute, default=0")
    parser.add_argument('--basic', help="Use HTTP Basic Auth to login", action="store_true")
    args = parser.parse_args()
    return args
'''
def main():
    #pdb.set_trace()
    host = sys.argv[1]
    port = sys.argv[2]

    if re.search('http://',host):
        url = host + port
    else:
        url = 'http://' + host + ':' + port

    '''
    argv = [ _ for _ in sys.argv]
    (args, _) = parser.parse_args(argv)
    '''
    try:
        execute(['scrapy', 'crawl', 'xsscrapy', 
                 '-a', 'url=%s' % url, '-a', 'user=%s' % None, '-a', 
                 'pw=%s' % None, '-a', 'basic=%s' % False, 
                 '-s', 'CONCURRENT_REQUESTS=%s' % '30',
                 '-s', 'DOWNLOAD_DELAY=%s' % '0'])
    except KeyboardInterrupt:
        sys.exit()

main()
