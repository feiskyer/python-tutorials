#!/usr/bin/python
# http://www.pythonchallenge.com/pc/def/equality.html

import urllib
import re
import string

def get_challenge(subject):
	text_src=urllib.urlopen('http://www.pythonchallenge.com/pc/def/%s.html' % subject).read()
	text=re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->',re.S).findall(text_src)[-1]
	return text

text=get_challenge('equality')

print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))

# Result:
# linkedlist
# Next level (4): http://www.pythonchallenge.com/pc/def/linkedlist.php
