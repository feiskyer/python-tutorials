#!/usr/bin/python
# coding: utf-8

# 题目中的原图是一张被打乱了图片。仔细观察一下就会发现，图片当中每一行都有一个
# 长度为 5 pixels 的粉色块。而且题目的标题为： 'let me get this straight' 。
# 因此猜测是需要把每一行的粉色块进行移位，使他们能够垂直对齐。即，使每一行从 
# '[粉块前][粉块][粉块后]' 变换到 '[粉块][粉块后][粉块前]' 。

import Image
import re
import urllib

url="http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif"
filename=url.split('/')[-1]
urllib.urlretrieve(url,filename)

img = Image.open("mozart.gif")
#转换数据为string并将本来可能存在的'\n'先替换掉
imgtext = img.tostring().replace('\n', '0')
#转换成640一行的格式
imgtext = '\n'.join([imgtext[i * 640: (i+1) * 640] for i in range(480)])
#对每一行用正则进行位置交换
#交换前：[粉块前][粉块][粉块后]
#交换后：[粉块][粉块后][粉块前]
#'\xc3' 为粉色像素的编码
imgtext = re.compile('^(.*?)(\xc3{5})(.*?)$', re.M).sub(r'\2\3\1', imgtext)
imgtext = imgtext.replace('\n', '')
img.fromstring(imgtext)
img.save("16.gif")

# 17 romance
