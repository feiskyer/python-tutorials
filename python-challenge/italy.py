#!/usr/bin/python
# coding: utf-8
# http://www.pythonchallenge.com/pc/return/italy.html

import urllib
import Image

# downlaod file with password
# user: huge passwd: file
url="http://huge:file@www.pythonchallenge.com/pc/return/wire.png"
filename=url.split('/')[-1]
urllib.urlretrieve(url,filename)

# tips
# remember: 100*100 = (100+99+99+98) + ... + (3+2+2+1) +1

im = Image.open("wire.png")
new = Image.new(im.mode, [100, 100])
#四个方向向量
vect=[(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, p, double_steps=-1, 0, 0, 200
#开始把像素往新图上盘
while p < 10000:
    for v in vect:
        for s in xrange(double_steps // 2):
            x, y = x + v[0], y + v[1]
            new.putpixel((x, y), im.getpixel((p, 0)))
            p = p + 1
        double_steps = double_steps - 1
new.save('14.jpg') 

# cat -> uzi
