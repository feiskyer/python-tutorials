#!/usr/bin/python
# coding: utf-8
# http://www.pythonchallenge.com/pc/return/disproportional.html

import urllib

# downlaod file with password
# user: huge passwd: file
url="http://huge:file@www.pythonchallenge.com/pc/phonebook.php"
filename=url.split('/')[-1]
urllib.urlretrieve(url,filename)

# from the php file:
# faultCode 105 
# faultString XML error: Invalid document end at line 1, column 1
# aparently, this is an xmlrpc error

import xmlrpclib

server=xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()
# Got: ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

print server.system.methodHelp('phone') 
# Got: Returns the phone of a person

print server.phone('Bert')	# 这里的Bert是上一关的提示信息
# Got 555-ITALY

# next level is italy