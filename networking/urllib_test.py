#!/usr/bin/python

import urllib
import sys

baidu = urllib.urlopen('http://www.baidu.com')
print 'http header:', baidu.info()
#print 'http status:', baidu.getcode() # getcode() will raise addinfourl instance has no attribute 'getcode' error
print 'url:', baidu.geturl()
# print baidu.read()
print urllib.quote("20 + 30 = 50")
print urllib.urlencode({'name':'zhangsan','age':20})
baidu.close()


def show_process(downloaded_blk_count, blk_size, total_size):
	per=100.0*downloaded_blk_count*blk_size/total_size
	if per>100:
		per=100
		sys.stdout.write('Downloading %.2f%%\r' % per)
		sys.stdout.write('\n')
	sys.stdout.write('Downloading %.2f%%\r' % per)
	sys.stdout.flush()

url='http://www.sina.com'
local='sina.html'
urllib.urlretrieve(url,local,show_process)
