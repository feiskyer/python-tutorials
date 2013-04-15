#!/usr/bin/python
# level (10): http://www.pythonchallenge.com/pc/return/bull.html
# login with user: huge passwd: file
#
# a = [1, 11, 21, 1211, 111221, 
# len(a[30])=?
#

# Look-and-say sequence problem

import re


s="1"
for i in range(30):
	s=''.join([ str(len(i+j))+i for i,j in re.findall(r'(\d)(\1*)',s)])

print len(s) # return 5808
 
