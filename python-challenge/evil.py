#!/usr/bin/python
# http://www.pythonchallenge.com/pc/return/evil.html

import urllib
import Image

# downlaod file with password
# user: huge passwd: file
url="http://huge:file@www.pythonchallenge.com/pc/return/evil1.jpg"
filename=url.split('/')[-1]
urllib.urlretrieve(url,filename)

# filename ends with 1, so we try to get more
for i in range(1,10):
	url="http://huge:file@www.pythonchallenge.com/pc/return/evil%d.jpg" % i
	filename=url.split('/')[-1]
	urllib.urlretrieve(url,filename)

# evil2.jpg shows "not jpg - .gfx"
# so we get evil2.gfx
url="http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx"
filename=url.split('/')[-1]
urllib.urlretrieve(url,filename)

# observe gfx file, no results ...

# deal the data into 5 equal piles and save those piles to disc
info = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx').read()  
for i in range(5):  
    file = open("evil_0%d.jpg" % i, "wb")  
    file.write(info[i::5])  
    file.close() 

# from image generated, we get disproportional

