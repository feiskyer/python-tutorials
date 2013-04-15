#!/usr/bin/python
import urllib2
import os
import re
import zlib
import gzip
from StringIO import StringIO

def get_url(url):
	content=''
	response = urllib2.urlopen(url)
	data = response.read()
	if response.info().get('Content-Encoding') == 'gzip':
		buff=StringIO(data)
		f=gzip.GzipFile(fileobj=buff)
		content=f.read()
	elif response.info().get('Content-Encoding') == 'deflate':
		content=zlib.decompress(data, -zlib.MAX_WBITS)
	else:
		content=data
	
	charset=re.search(r'charset=([\w-]+)', response.headers['content-type'])
	if charset:
		charset=charset.group(1)
	if charset:
		content=content.decode(charset)
	return content

def url_size(url):
	request = urllib2.Request(url)
	request.get_method = lambda: 'HEAD'
	response = urllib2.urlopen(request)
	size = int(response.headers['content-length'])
	return size

def url_save(url, filepath, refer=None):
	# add http headers
	headers = {}
	if refer:
		headers['Referer'] = refer
	request = urllib2.Request(url, headers=headers)
	# add post data
	# urllib2.Request(url, headers=headers, 
	# 					data='person=jessinio&gender=male') 
	response = urllib2.urlopen(request)
	file_size = int(response.headers['content-length'])
	assert file_size
	if os.path.exists(filepath):
		if file_size == os.path.getsize(filepath):
			print 'Skip %s: file already exists' % os.path.basename(filepath)
			return
		else:
			print 'Overwriting', os.path.basename(filepath), '...'
	with open(filepath, 'wb') as output:
		received = 0
		while True:
			buffer = response.read(1024*256)
			if not buffer:
				break
			received += len(buffer)
			output.write(buffer)
	assert received == file_size == os.path.getsize(filepath), '%s == %s == %s' % (received, file_size, os.path.getsize(filepath))

def show_process(downloaded_blk_count, blk_size, total_size):
	import sys
	per=100.0*downloaded_blk_count*blk_size/total_size
	if per>100:
		per=100
		sys.stdout.write('Downloading %.2f%%\r' % per)
		sys.stdout.write('\n')
	sys.stdout.write('Downloading %.2f%%\r' % per)
	sys.stdout.flush()

def url_save2(url, local):	# use urllib.urlretireve to download file
	import urllib
	urllib.urlretrieve(url,local,show_process)

if __name__=='__main__':
	try:
		#print get_url('http://www.baidu.com')
		print url_size('http://www.baidu.com')
		#url_save2('http://www.baidu.com','baidu.html')
		url_save('http://www.baidu.com','baidu.html')
	except:
		#import traceback
		#import sys
		#traceback.print_exc(file=sys.stdout)
		print 'Can\'t download file '

