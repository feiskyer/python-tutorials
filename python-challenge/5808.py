#!/usr/bin/python
# http://www.pythonchallenge.com/pc/return/5808.html

import urllib
import Image

url="http://www.pythonchallenge.com/pc/return/cave.jpg"
filename=url.split('/')[-1]
urllib.urlretrieve(url,filename)	# user: huge passwd: file
img=Image.open(filename)
w,h=img.size

im=Image.new('RGB', (w/2,h/2))
for i in range(w):
	for j in range(h):
		if i%2==0 and j%2==0:
			im.putpixel((i / 2, j/ 2), img.getpixel((i,j)))

im.save('even.png')

# from the picture, we know next level is evil
