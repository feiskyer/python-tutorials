#!/usr/bin/python
# http://www.pythonchallenge.com/pc/def/ocr.html

import urllib
import re
import string

def get_challenge():
	text_src=urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
	text=re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->',re.S).findall(text_src)[-1]
	return text

text=get_challenge()
counts={}
for c in text:
	counts[c]=counts.get(c,0)+1
	# {'\n': 1221, '!': 6079, '#': 6115, '%': 6104, '$': 6046, '&': 6043, ')': 6186, '(': 6154, '+': 6066, '*': 6034, '@': 6157, '[': 6108, ']': 6152, '_': 6112, '^': 6030, 'a': 1, 'e': 1, 'i': 1, 'l': 1, 'q': 1, 'u': 1, 't': 1, 'y': 1, '{': 6046, '}': 6105}

# Method I
avg=len(text)/len(counts)
print ''.join([c for c in text if c!='\n' and counts[c]<avg])

# Method II: Find all characters
print ''.join(re.compile('[a-z]').findall(text))
print filter(lambda x:x in string.letters, text)

# equality
# next level: http://www.pythonchallenge.com/pc/def/equality.html
