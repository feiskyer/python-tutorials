#!/usr/bin/python

# http://www.pythonchallenge.com/pc/def/map.html
import string 
tr=string.maketrans(string.lowercase,string.lowercase[2:]+string.lowercase[:2])
s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print s.translate(tr)
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print 'map'.translate(tr)
# ocr 
# next level: http://www.pythonchallenge.com/pc/def/ocr.html
