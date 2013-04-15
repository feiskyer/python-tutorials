#!/usr/bin/env python

import urllib2 
import socket

def _get_my_ip():
    """
    Returns the actual ip of the local machine.

    This code figures out what source address would be used if some traffic
    were to be sent out to some well known address on the Internet. In this
    case, a Google DNS server is used, but the specific address does not
    matter much.  No traffic is actually sent.
    """
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"


def set_proxy():
    proxy = '127.0.0.1:8087' 
    opener = urllib2.build_opener( urllib2.ProxyHandler({'http':proxy}) )
    urllib2.install_opener( opener ) 

if __name__=='__main__':
    url = 'http://ifconfig.me/ip'
    print urllib2.urlopen(url).read()
    print _get_my_ip()

    set_proxy()
    print urllib2.urlopen(url).read()
    print _get_my_ip()

